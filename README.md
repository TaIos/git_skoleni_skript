# GIT školení skript
## 1. Úvod
## 2. GIT Object Model
## 3. Instalace GITu
## 4. Interaktivní demo
### Základ
* `git init` (initialize)
	* `.git/objects`
	* `.git/config`
	* `.git/hooks`
* `git help <command>`
* `git status`
* vytvořit README.md
* vysvětlit staging area
	* `git status`
	* `git add <file>`
	* `git status`
* `git commit`
	* `git cat-file -t <hash>`
	* `git cat-file -p <hash>`
* `git log --all --graph --oneline`
* popsat reference
	* vizuální příklad v [větvením](https://learngitbranching.js.org/?NODEMO=&locale=en_US)
* další commit
	* popsat posouvání referencí
* `git checkout <hash|branch>`
	* zmeni ukazatel `HEAD` a obsah working directory 
* `git checkout master`
	* edit
	* `git stash`
	* `git stash list`
	* `git stash pop`
	* alternativa `git checkout -f`
* `git diff [<commit>] [<path>]`
	* rodzil oproti `HEAD`

### Branching & merging

* *script.py*
```
import sys

def default():
    print("Hello")

def main():
    default()

if __name__ == "__main__":
    main()
```
* `git branch`
* `git branch <name(cat)>`
	* `git checkout cat`
	* `git branch -vv`
* přidat 
```
sys.argv[1]
```
	* `git status`
	* `git commit`
* `git checkout master`
	* popsat
* `git branch dog; git checkout dog;` == `git checkout -b dog`
	* doplnit *dog* feature
	* `git commit`
	* popsat `git log` graf
	* [vizualizace](https://learngitbranching.js.org/?NODEMO=&locale=en_US)
* `git merge <branch(cat)>`	
	* popsat Fast-forward
	* [vizualizace](https://learngitbranching.js.org/?NODEMO=&locale=en_US)
* `git merge dog`
	* popsat Merge-conflict
	* `git merge --continue`

### Nahrávání změn do vzdáleného repozitáře

* `git remote`
* `GitHub – vytvoření repozitáře`
* `git remote add <name> <url>`
* `git push <remote> <local branch>:<remote branch>`
* upravit README
	* `git commit`
	* `git log` → popsat `origin/master` vs `master`
* `git branch --set-upstream-to=origin/master` | `git push -u origin master`
* `git branch -vv`
* `git push`

### Stáhnutí repozitáře

* `git clone <url> [folder name]`
* nasimulovat commit a push prvního programátora (upravit README)
* druhý programátor vytvoří `cow` funkcionalitu
	* `git push` → odmítnuto
	* `git fetch`
	* `git merge origin/master`
	* `git pull` = `git fetch; git merge origin/master`
* shrnuti
	* `git remote`, `git push`, `git fetch`, `git merge`, `git pull`

<p align="center">
<b>OTÁZKY ???</b><br>
(příkazy pro nastavování jsou příšerné)
</p>

### Další užitečné příkazy
* `git add -p`
	* nápověda `?`
* `git commit --amend --no-edit`
* zrušení psaní commit message prázdným obsahem
* `git add .`
* `git checkout -`
* `git revert <hash>`
* `git blame [commit] <file>`
	* `git blame 8acab378ae40c4d0695b330e9ac14ce1b09977b5 Java\ Development/zlbpwa_api/src/zlbpwa/api/service/SampleCardService.java`
	* rádka 125
	* ukázat `blame` na GitHubu

## 5. Konfigurační soubory
* `~/.gitconfig` vs `.git/config`

## 6. Gitignore
* https://github.com/github/gitignore
* `DS_Store`


## 7. Závěr
