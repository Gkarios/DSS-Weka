def convert_tree_to_code(tree_structure):
    lines = tree_structure.strip().split('\n')
    code_lines = ["def predict(G1, absences, Fjob, reason, failures, age, goout, Mjob, Pstatus, activities, Fedu, famrel):"]
    indentation_level = 0

    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            # Count the number of '|   ' to determine the indentation level
            parts = stripped_line.split('|')
            new_indentation_level = len(parts) - 1
            condition_or_value = parts[-1].strip()

            # Handle leaf nodes (those with return values)
            if ':' in condition_or_value:
                condition, value = condition_or_value.split(':')
                condition = condition.strip()
                value = value.strip().split()[0]  # Only get the first part of the value
                if condition:
                    if indentation_level > 0:
                        code_lines.append('    ' * (new_indentation_level - 1) + "elif " + condition + ":")
                    else:
                        code_lines.append('    ' * new_indentation_level + f"if {condition}:")
                    new_indentation_level += 1
                code_lines.append('    ' * new_indentation_level + f"return {value}")
            else:
                # Handle condition nodes
                while indentation_level > new_indentation_level:
                    indentation_level -= 1
                    code_lines.append('    ' * indentation_level + "elif:")
                if indentation_level == 0:
                    code_lines.append('    ' * new_indentation_level + f"if {condition_or_value}:")
                else:
                    code_lines.append('    ' * new_indentation_level + f"elif {condition_or_value}:")

            indentation_level = new_indentation_level

    # Close any remaining open blocks with else:
    while indentation_level > 0:
        indentation_level -= 1
        code_lines.append('    ' * indentation_level + "else:")

    return "\n".join(code_lines)

tree_structure = """
failures < 0.5
|   higher = yes
|   |   studytime < 1.5 : 11.92 (91/6.15) [50/6.15]
|   |   studytime >= 1.5
|   |   |   schoolsup = yes
|   |   |   |   Fjob = teacher : 12.33 (6/1.22) [0/0]
|   |   |   |   Fjob = other : 11.79 (20/2.01) [9/6.09]
|   |   |   |   Fjob = services : 9 (3/2) [4/26.25]
|   |   |   |   Fjob = health : 11.25 (2/1) [2/2.5]
|   |   |   |   Fjob = at_home : 12.33 (2/4) [1/1]
|   |   |   schoolsup = no
|   |   |   |   traveltime < 2.5
|   |   |   |   |   studytime < 2.5
|   |   |   |   |   |   Fjob = teacher : 15.18 (9/5.58) [2/6.09]
|   |   |   |   |   |   Fjob = other
|   |   |   |   |   |   |   Mjob = at_home : 11.54 (8/3.5) [5/3.05]
|   |   |   |   |   |   |   Mjob = health : 13.45 (7/4.78) [4/1.9]
|   |   |   |   |   |   |   Mjob = other
|   |   |   |   |   |   |   |   famrel < 3.5 : 10.57 (3/0.22) [4/10.19]
|   |   |   |   |   |   |   |   famrel >= 3.5
|   |   |   |   |   |   |   |   |   Walc < 1.5
|   |   |   |   |   |   |   |   |   |   famsup = no : 12 (6/3.47) [5/5.36]
|   |   |   |   |   |   |   |   |   |   famsup = yes
|   |   |   |   |   |   |   |   |   |   |   reason = course : 12.6 (4/0.25) [1/0.25]
|   |   |   |   |   |   |   |   |   |   |   reason = other : 13.82 (0/0) [0/0]
|   |   |   |   |   |   |   |   |   |   |   reason = home : 13 (3/0) [0/0]
|   |   |   |   |   |   |   |   |   |   |   reason = reputation : 16.67 (2/1) [1/4]
|   |   |   |   |   |   |   |   |   Walc >= 1.5 : 14.26 (16/7.11) [11/2.16]
|   |   |   |   |   |   |   Mjob = services : 13.95 (16/3.31) [6/6]
|   |   |   |   |   |   |   Mjob = teacher : 12.11 (11/4.38) [7/25.2]
|   |   |   |   |   |   Fjob = services : 12.29 (30/6.09) [22/19.7]
|   |   |   |   |   |   Fjob = health : 13.33 (6/8.81) [3/11.81]
|   |   |   |   |   |   Fjob = at_home : 13.56 (6/4.22) [3/10.11]
|   |   |   |   |   studytime >= 2.5
|   |   |   |   |   |   reason = course : 13.58 (28/4.68) [10/7.44]
|   |   |   |   |   |   reason = other : 16 (6/1.67) [0/0]
|   |   |   |   |   |   reason = home
|   |   |   |   |   |   |   absences < 5.5
|   |   |   |   |   |   |   |   Mjob = at_home : 14 (2/1) [0/0]
|   |   |   |   |   |   |   |   Mjob = health : 14 (1/0) [0/0]
|   |   |   |   |   |   |   |   Mjob = other
|   |   |   |   |   |   |   |   |   sex = F : 13 (3/0.22) [2/3.78]
|   |   |   |   |   |   |   |   |   sex = M : 15.33 (2/0) [1/1]
|   |   |   |   |   |   |   |   Mjob = services : 14.67 (3/0.22) [0/0]
|   |   |   |   |   |   |   |   Mjob = teacher : 15 (1/0) [1/4]
|   |   |   |   |   |   |   absences >= 5.5 : 12 (2/0.25) [1/2.25]
|   |   |   |   |   |   reason = reputation
|   |   |   |   |   |   |   age < 16.5
|   |   |   |   |   |   |   |   Mjob = at_home : 12 (0/0) [1/3.57]
|   |   |   |   |   |   |   |   Mjob = health : 17 (1/0) [0/0]
|   |   |   |   |   |   |   |   Mjob = other : 13.17 (5/1.44) [1/6.76]
|   |   |   |   |   |   |   |   Mjob = services : 13 (3/0.22) [1/1.78]
|   |   |   |   |   |   |   |   Mjob = teacher : 13.33 (0/0) [0/0]
|   |   |   |   |   |   |   age >= 16.5
|   |   |   |   |   |   |   |   studytime < 3.5 : 14.38 (6/2.89) [7/9.83]
|   |   |   |   |   |   |   |   studytime >= 3.5 : 16.71 (4/0.69) [3/12.06]
|   |   |   |   traveltime >= 2.5
|   |   |   |   |   reason = course
|   |   |   |   |   |   goout < 4.5 : 14.2 (6/4.81) [4/1.19]
|   |   |   |   |   |   goout >= 4.5 : 10 (3/0.22) [2/0.94]
|   |   |   |   |   reason = other : 7.83 (4/18.69) [2/4.06]
|   |   |   |   |   reason = home : 12 (3/0.67) [0/0]
|   |   |   |   |   reason = reputation : 14 (3/0.67) [0/0]
|   higher = no : 9.89 (27/3.41) [9/1.56]
failures >= 0.5 : 8.59 (68/13.6) [32/4.9]
"""

python_code = convert_tree_to_code(tree_structure)
print(python_code)

