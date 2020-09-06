# GIT školení skript
## 1. GIT Object Model
## 2. Interaktivní demo
### Základ
* `git init` (initialize)
	* `.git/objects`
	* `.git/refs`
	* `.git/config`
	* `.git/hooks`
* `git help init`
* `git status`
	* popis výstupu
* vytvořit soubor
* vysvětlit staging area
	* `git status`
	* `git add <file>`
	* `git status`
* `git commit`
	* graficky vysvětlit
	* `git cat-file -p <hash>`
* `git log --all --graph --oneline`
* popsat reference
	* `master`, `HEAD`
* `git checkout <hash>`
	* zmeni ukazatel `HEAD` a obsah working directory 
	* `HEAD x master`
* `git checkout master`
	* edit
	* `git stash`
	* `git stash list`
	* `git stash pop`
	* alternativa `git checkout -f`
* `git diff [<commit>] [<path>]`
	* rodzil oproti `HEAD`

### Branching & merging

* python skript
```
import sys

def default():
    print("Hello")

def main():
    default()

if __name__ == "__main__":
    main()
```
* `git branch`, `git branch -vv`
* `git ranch cat`
	* popsat (pointer update)
	* `git checkout cat`
* přidat 
```
sys.argv[1]
```
	* `git status`
	* `git diff`
	* `git commit`
* `git checkout master`
	* popsat
* `git branch dog; git checkout dog;` == `git checkout -b dog`
	* `git commit`
	* popsat `git log` graf
* `git merge cat`	
	* popsat Fast-forward
* `git merge dog`
	* popsat Merge-conflict
	* `git add <file>`
	* `git merge --continue`
	* popsat historii
### Nahrávání změn do vzdáleného repozitáře
* `git remote`
	* vypíše všechny remoty
* `GitHub – vytvoření repozitáře`
* `git remote add <name> <url>`
* `git push <remote> <local branch>:<remote branch>`
* `git commit`
	* popsat `origin/master` vs `master`
* `git branch --set-upstream-to=origin/master` | `git push -u origin master`
* `git branch -vv`

### Stáhnutí repozitáře
* `git clone <url> [folder name]`
	* nasimulovat commit od druheho programatora
* `git fetch`
* `git git merge origin/master`
* `git pull --all`
* shrnuti
	* `git remote`, `git push`, `git fetch` nasledovaný `git merge`, `git pull`
	* `git pull`

<p align="center">
<b>OTÁZKY ???</b><br>
(příkazy pro nastavování jsou příšerné)
</p>

## 3. Honorable mentions

### Konfigurační soubory
* `~/.gitconfig` vs `.git/config`

### Gitignore
* https://github.com/github/gitignore
* `DS_Store`

#### Další užitečné příkazy
* `git blame`
	* pripravit priklad s Petrem Schmiedem
* `git add -p`
* `git commit --amend --no-edit`
* zrušení psaní commit message prázdným obsahem
* `git stash` pro umožnění checkout
* `git add .`
* `git merge -`
* `git revert <hash>`

## 4. Závěr
