from pathlib import Path #path is just a class in pathlab module, show the file path
from git import Repo #Repo class can interact with a git repository and make/delete directorys

#--- setup ---------------------------------------------------------------
repo_path = Path("/workspaces/MSSP6070/")     # path to your local clone
folder     = repo_path/"WeeklyModules/Week08"   # folder you want to add
commit_msg = "Add Weekly Module folder with placeholder"

# --- create the folder & placeholder -------------------------------------
folder.mkdir(parents=True, exist_ok=True) #make the directory(文件夹)
(folder / ".gitkeep").touch()  # ensures Git tracks and keep an empty dir

# --- stage, commit, push --------------------------------------------------
repo = Repo(repo_path)
repo.index.add([str(p.relative_to(repo_path)) for p in folder.rglob("*")])
repo.index.commit(commit_msg)

origin = repo.remote(name="origin")
origin.push()                               # push to the same branch
print("✅ Folder pushed!")