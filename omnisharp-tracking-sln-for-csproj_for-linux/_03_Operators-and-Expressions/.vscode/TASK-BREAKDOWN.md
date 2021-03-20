
# # Bash Script TASK BREAKDOWN

# Bare minimum (manually executable)
## 1. Read *.sln and collect all :
    # Projects  .... "Project_Name", "Project_Name.csproj"
## 2. Check if there are changes between the existing list of projects and the newly collected list from *.sln
    # If there is:
        # rebuild the launch.json
        # rebuild the tasks.json
# Extras:
# 3. Instead of rebuilding the 2*.json files used by omnisharp to debug execute:
    # comment old and add new
    # have option to clear the commented/old/substituted projects
# Future Direction (automated):
## 4. Add a form of watch* functionality, or a small server, or a service (pro/con it first)