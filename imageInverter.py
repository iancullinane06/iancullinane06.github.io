import argparse
import re
from pathlib import Path

from PIL import Image, ImageColor, ImageOps

SUPPORTED_EXTENSIONS = {".bmp", ".gif", ".jpeg", ".jpg", ".png", ".svg", ".tif", ".tiff"}
COLOR_PROPERTIES = (
	"fill",
	"stroke",
	"color",
	"stop-color",
	"flood-color",
	"lighting-color",
)
COLOR_PATTERN = re.compile(
	rf"(?P<prefix>\b(?:{'|'.join(COLOR_PROPERTIES)})\s*[=:]\s*)(?P<quote>['\"]?)"
	rf"(?P<color>[^;\"']+?)(?P=quote)(?=[;\s>]|$)",
	re.IGNORECASE,
)


def invert_color(color: str) -> str:
	"""Invert a CSS color while preserving its alpha channel."""
	value = color.strip()
	if value.startswith(("url(", "var(", "currentColor")) or value in {
		"none",
		"inherit",
		"initial",
		"unset",
	}:
		return color

	try:
		red, green, blue, *alpha = ImageColor.getcolor(value, "RGBA")
	except ValueError:
		return color

	inverted = (255 - red, 255 - green, 255 - blue, *alpha)
	if alpha and alpha[0] != 255:
		return f"rgba({inverted[0]}, {inverted[1]}, {inverted[2]}, {inverted[3] / 255:g})"
	return f"#{inverted[0]:02x}{inverted[1]:02x}{inverted[2]:02x}"


def invert_svg(svg_path: Path) -> Path:
	"""Invert colors in an SVG and preserve its vector structure."""
	svg = svg_path.read_text(encoding="utf-8")

	def replace_color(match: re.Match[str]) -> str:
		return (
			f"{match.group('prefix')}{match.group('quote')}"
			f"{invert_color(match.group('color'))}{match.group('quote')}"
		)

	inverted = COLOR_PATTERN.sub(replace_color, svg)
	svg_path.write_text(inverted, encoding="utf-8")
	return svg_path

def invert_image(image_path: Path) -> Path:
	"""Save an inverted copy of the image and return its path."""
	if image_path.suffix.lower() == ".svg":
		return invert_svg(image_path)

	with Image.open(image_path) as image:
		alpha = image.getchannel("A") if "A" in image.getbands() else None
		inverted = ImageOps.invert(image.convert("RGB"))
		if alpha is not None:
			inverted.putalpha(alpha)

		output_path = image_path.with_name(
			f"{image_path.stem}{image_path.suffix}"
		)
		inverted.save(output_path)

	return output_path


def get_image_paths(input_path: Path) -> list[Path]:
	"""Return supported images from a file or directory."""
	if input_path.is_file():
		if input_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
			raise ValueError(f"Unsupported image type: {input_path.suffix or '(none)'}")
		return [input_path]

	if input_path.is_dir():
		return sorted(
			path
			for path in input_path.rglob("*")
			if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
		)

	raise FileNotFoundError(f"Path does not exist: {input_path}")


def main() -> None:
	parser = argparse.ArgumentParser(description="Invert image colors.")
	parser.add_argument(
		"input_path",
		type=Path,
		help="path to an image file or a directory of images",
	)
	args = parser.parse_args()

	try:
		image_paths = get_image_paths(args.input_path)
	except (FileNotFoundError, ValueError) as error:
		parser.error(str(error))

	for image_path in image_paths:
		output_path = invert_image(image_path)
		print(f"Inverted image saved to: {output_path}")

	if not image_paths:
		parser.error(f"No supported images found in: {args.input_path}")


if __name__ == "__main__":
	main()
