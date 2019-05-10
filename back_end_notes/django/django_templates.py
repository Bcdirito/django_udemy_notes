# Templates Notes

# Contain the static aspects of page

# Special Tags/Syntax & HTML

# Start by creating templates directory in top level

# Templates dictionary in settings.py

# render()

# To get template path add TEMPLATE_DIR = os.path.join(BASE_DIR, "templates") to the settings.py file

# Variables are declared in HTML files as {{ variable_name }}
# Views functions always return render(request, "directory_name/file_name.html", context="variable_name")