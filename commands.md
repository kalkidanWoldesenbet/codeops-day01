# Commands Used – Day 1 Practical Exercise

## Part 1: Create the project structure

```bash
mkdir -p codeops/module1/day01
cd codeops/module1/day01
touch README.md notes.txt commands.md
```

## Add content to README.md

```bash
echo "# CodeOps Day 1" > README.md
echo "Student Name:" >> README.md
echo "Date:" >> README.md
```

## Add content to notes.txt

```bash
echo "Today I learned:" > notes.txt
echo "- Terminal" >> notes.txt
echo "- Git" >> notes.txt
echo "- GitHub" >> notes.txt
```

## Display file contents

```bash
cat README.md
cat notes.txt
```

## Part 2: Terminal commands

```bash
pwd
ls -la
mv notes.txt terminal-notes.txt
cp README.md README-copy.md
mkdir backup
mv README-copy.md backup/
tree

```

## Part 3: Git commands

```bash
git init
git status
git add .
git commit -m "Initial commit with day01 files"
```

## Update README.md and make second commit

```bash
echo "This project contains Day 1 terminal, Git, and GitHub practice tasks." >> README.md
git status
git add README.md
git commit -m "Update README with project description"
git log --oneline
```

## Part 4: GitHub commands

```bash
git remote add origin https://github.com/YOUR-USERNAME/codeops-day01.git
git branch -M main
git push -u origin main
```

## Part 5: Reflection and bonus files

```bash
touch reflection.md
touch .gitignore
echo "node_modules/" > .gitignore
echo ".env" >> .gitignore
echo "*.log" >> .gitignore
touch .env
git status
git add .
git commit -m "Add reflection and gitignore files"
git push
```
