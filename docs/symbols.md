# Mathematical symbols

```python
from labplotlib import print_symbols, search, symbols
```

## `symbols`

A read-only mapping from descriptive names to Unicode strings. Some values,
such as `"degree_celsius"`, contain more than one character.

```python
from labplotlib import symbols

print(symbols["sigma"])   # σ
print(symbols["squared"]) # ²
print(symbols["planet_earth"])  # ♁
```

Planetary symbols are available for Mercury through Neptune. Pluto's
traditional planetary symbol is also included as `planet_pluto`.

## Symbol list

The complete symbol mapping is listed below. The names are the keys used with
`symbols` and `search`.

| Name | Symbol |
| --- | --- |
| `set_empty` | ∅ |
| `set_union` | ∪ |
| `set_intersection` | ∩ |
| `set_is_element_of` | ∈ |
| `set_is_not_element_of` | ∉ |
| `set_is_subset_of` | ⊆ |
| `set_is_proper_subset_of` | ⊂ |
| `set_is_not_subset_of` | ⊄ |
| `set_is_superset_of` | ⊇ |
| `set_is_proper_superset_of` | ⊃ |
| `set_is_not_superset_of` | ⊅ |
| `set_universal` | 𝕌 |
| `set_minus` | ∖ |
| `set_cartesian_product` | × |
| `set_difference` | \ |
| `delta` | Δ |
| `set_cardinality` | \| |
| `set_complement` | ' |
| `set_power_set` | ℙ |
| `set_contains_as_member` | ∋ |
| `set_does_not_contain_as_member` | ∌ |
| `complex_numbers` | ℂ |
| `real_numbers` | ℝ |
| `rational_numbers` | ℚ |
| `integers` | ℤ |
| `natural_numbers` | ℕ |
| `superscript_i` | ⁱ |
| `superscript_n` | ⁿ |
| `superscript_plus_sign` | ⁺ |
| `superscript_minus` | ⁻ |
| `superscript_zero_0` | ⁰ |
| `superscript_one_1` | ¹ |
| `squared` | ² |
| `cubed` | ³ |
| `superscript_four_4` | ⁴ |
| `superscript_five_5` | ⁵ |
| `superscript_six_6` | ⁶ |
| `superscript_seven_7` | ⁷ |
| `superscript_eight_8` | ⁸ |
| `superscript_nine_9` | ⁹ |
| `subscript_zero_0` | ₀ |
| `subscript_one_1` | ₁ |
| `subscript_two_2` | ₂ |
| `subscript_three_3` | ₃ |
| `subscript_four_4` | ₄ |
| `subscript_five_5` | ₅ |
| `subscript_six_6` | ₆ |
| `subscript_seven_7` | ₇ |
| `subscript_eight_8` | ₈ |
| `subscript_nine_9` | ₉ |
| `fraction_one_half_1_2` | ½ |
| `fraction_zero_thirds_0_3` | ↉ |
| `fraction_one_third_1_3` | ⅓ |
| `fraction_two_thirds_2_3` | ⅔ |
| `fraction_one_quarter_1_4` | ¼ |
| `fraction_three_quarters_3_4` | ¾ |
| `fraction_one_fifth_1_5` | ⅕ |
| `fraction_two_fifths_2_5` | ⅖ |
| `fraction_three_fifths_3_5` | ⅗ |
| `fraction_four_fifths_4_5` | ⅘ |
| `fraction_one_sixth_1_6` | ⅙ |
| `fraction_five_sixths_5_6` | ⅚ |
| `fraction_one_seventh_1_7` | ⅐ |
| `fraction_one_eighth_1_8` | ⅛ |
| `fraction_three_eighths_3_8` | ⅜ |
| `fraction_five_eighths_5_8` | ⅝ |
| `fraction_seven_eighths_7_8` | ⅞ |
| `fraction_one_ninth_1_9` | ⅑ |
| `fraction_one_tenth_1_10` | ⅒ |
| `degree` | ° |
| `degree_celsius` | °C |
| `degree_fahrenheit` | °F |
| `diameter` | ⌀ |
| `multiplication` | × |
| `division` | ÷ |
| `left_floor` | ⌊ |
| `right_floor` | ⌋ |
| `left_ceiling` | ⌈ |
| `right_ceiling` | ⌉ |
| `product` | ∏ |
| `coproduct` | ∐ |
| `summation` | ∑ |
| `summation_top` | ⎲ |
| `summation_bottom` | ⎳ |
| `partial_differential` | ∂ |
| `integral` | ∫ |
| `top_half_integral` | ⌠ |
| `bottom_half_integral` | ⌡ |
| `not_sign` | ¬ |
| `plus_minus` / `pm` | ± |
| `square_root` | √ |
| `cube_root` | ∛ |
| `fourth_root` | ∜ |
| `proportional_to` | ∝ |
| `infinity` | ∞ |
| `right_angle` | ∟ |
| `angle` | ∠ |
| `therefore` | ∴ |
| `approximately_equal_to` | ≈ |
| `congruent_to` | ≅ |
| `not_equal_to` | ≠ |
| `less_than_or_equal_to` | ≤ |
| `greater_than_or_equal_to` | ≥ |
| `right_angle_with_arc` | ⊾ |
| `right_triangle` | ⊿ |
| `dot_operator` | ⋅ |
| `sigma` | σ |
| `planet_mercury` | ☿ |
| `planet_venus` | ♀ |
| `planet_earth` | ♁ |
| `planet_mars` | ♂ |
| `planet_jupiter` | ♃ |
| `planet_saturn` | ♄ |
| `planet_uranus` | ♅ |
| `planet_neptune` | ♆ |
| `planet_pluto` | ♇ |

## `search(namelike)`

Find symbols whose names contain a substring, without case sensitivity.

| Parameter | Meaning |
| --- | --- |
| `namelike` | String to search for in symbol names. An empty string matches every name. |

**Returns:** a read-only mapping of matching names to symbol strings; it may
be empty.

```python
from labplotlib import search

print(dict(search("sigma")))  # {'sigma': 'σ'}
```

## `print_symbols(symbols_to_print=symbols)`

Print names, symbol values, and their decimal and hexadecimal Unicode code
points.

| Parameter | Meaning |
| --- | --- |
| `symbols_to_print` | Mapping of names to symbol strings; defaults to all library symbols. |

**Returns:** `None`; writes to standard output.

```python
from labplotlib import print_symbols, search

print_symbols(search("sigma"))
```
