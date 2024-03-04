# functions with outputs

def format_name(f_name, l_name):
    """Take a first and last name. Return it as a title case formatted name.

    Args:
        f_name (str): first name
        l_name (str): last name
    """
    f_title_name = f_name.title()
    l_title_name = l_name.title()
    return(f"{f_title_name} {l_title_name}")

print(format_name("NiCk", "hofMEIster"))

format_name()