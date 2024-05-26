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
G1 < 11.5
|   G1 < 8.5
|   |   absences < 1 : 5 (19/19.57) [11/20.23]
|   |   absences >= 1
|   |   |   Fjob = teacher : 11 (1/0) [0/0]
|   |   |   Fjob = other
|   |   |   |   reason = course : 8.86 (17/1.24) [4/0.92]
|   |   |   |   reason = other : 8 (3/0.22) [2/0.94]
|   |   |   |   reason = home : 9.2 (4/0.5) [1/1]
|   |   |   |   reason = reputation : 9.83 (5/1.2) [1/1]
|   |   |   Fjob = services
|   |   |   |   reason = course : 8.5 (5/0.16) [3/3.31]
|   |   |   |   reason = other : 5.5 (1/0) [1/1]
|   |   |   |   reason = home : 8.5 (1/0) [1/1]
|   |   |   |   reason = reputation : 8 (2/0) [1/0]
|   |   |   Fjob = health : 7 (2/1) [0/0]
|   |   |   Fjob = at_home : 8.29 (3/1.56) [4/1.19]
|   G1 >= 8.5
|   |   failures < 0.5
|   |   |   G1 < 10.5
|   |   |   |   absences < 20
|   |   |   |   |   age < 16.5
|   |   |   |   |   |   absences < 1.5
|   |   |   |   |   |   |   Mjob = at_home : 9.25 (2/0.25) [2/0.25]
|   |   |   |   |   |   |   Mjob = health : 11 (1/0) [0/0]
|   |   |   |   |   |   |   Mjob = other : 11 (6/0) [1/0]
|   |   |   |   |   |   |   Mjob = services : 11.71 (5/1.36) [2/12.24]
|   |   |   |   |   |   |   Mjob = teacher : 12 (1/0) [0/0]
|   |   |   |   |   |   absences >= 1.5 : 10.21 (24/1.21) [14/1.03]
|   |   |   |   |   age >= 16.5
|   |   |   |   |   |   reason = course
|   |   |   |   |   |   |   Fjob = teacher : 9 (1/0) [0/0]
|   |   |   |   |   |   |   Fjob = other
|   |   |   |   |   |   |   |   goout < 4.5
|   |   |   |   |   |   |   |   |   Mjob = at_home : 10.8 (3/0) [2/0.5]
|   |   |   |   |   |   |   |   |   Mjob = health : 11.27 (0/0) [0/0]
|   |   |   |   |   |   |   |   |   Mjob = other : 12.33 (1/0) [2/0.5]
|   |   |   |   |   |   |   |   |   Mjob = services : 11 (1/0) [0/0]
|   |   |   |   |   |   |   |   |   Mjob = teacher : 11 (2/0) [0/0]
|   |   |   |   |   |   |   |   goout >= 4.5 : 10.67 (5/0.24) [1/2.56]
|   |   |   |   |   |   |   Fjob = services : 10.11 (2/0) [7/0.71]
|   |   |   |   |   |   |   Fjob = health : 10.58 (0/0) [0/0]
|   |   |   |   |   |   |   Fjob = at_home : 10 (2/0) [2/0]
|   |   |   |   |   |   reason = other : 10.2 (3/0.89) [2/1.61]
|   |   |   |   |   |   reason = home
|   |   |   |   |   |   |   Pstatus = A : 13.5 (2/0.25) [0/0]
|   |   |   |   |   |   |   Pstatus = T
|   |   |   |   |   |   |   |   activities = no : 10.88 (7/0.29) [1/1]
|   |   |   |   |   |   |   |   activities = yes : 12.25 (4/0.19) [0/0]
|   |   |   |   |   |   reason = reputation : 11.57 (7/1.39) [0/0]
|   |   |   |   absences >= 20 : 7.5 (2/2.25) [0/0]
|   |   |   G1 >= 10.5
|   |   |   |   absences < 8.5
|   |   |   |   |   reason = course
|   |   |   |   |   |   Fedu < 2.5 : 11.35 (11/1.69) [9/1.74]
|   |   |   |   |   |   Fedu >= 2.5 : 13 (7/0.69) [4/1.84]
|   |   |   |   |   reason = other : 11.58 (9/1.14) [3/2.31]
|   |   |   |   |   reason = home : 12 (12/1.41) [5/2.41]
|   |   |   |   |   reason = reputation : 11.65 (10/1.44) [7/2.22]
|   |   |   |   absences >= 8.5 : 10.38 (5/0.64) [3/0.23]
|   |   failures >= 0.5 : 9.37 (29/9.72) [20/1.89]
G1 >= 11.5
|   G1 < 13.5 : 12.89 (25/3.61) [5/5.11]
|   G1 >= 13.5
|   |   G1 < 15.5
|   |   |   age < 16.5 : 14.34 (18/2.1) [2/3.15]
|   |   |   age >= 16.5
|   |   |   |   famrel < 3.5 : 14.18 (9/2.12) [1/0.75]
|   |   |   |   famrel >= 3.5 : 15.64 (6/0.8) [4/0.6]
|   |   G1 >= 15.5
|   |   |   G1 < 16.5 : 16.45 (7/0.5) [0/0]
|   |   |   G1 >= 16.5 : 17.54 (2/0.5) [0/0]
"""

python_code = convert_tree_to_code(tree_structure)
print(python_code)

