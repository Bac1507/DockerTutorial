Git la he thong kiem soat phien ban VCS.
Cac lenh thuong dung trong Git:
- git init
- git config
- git add
- git comit
- git checkout --ten_file
- git branch
- git checkout -b ten_branch
- git checkout -D ten_branch
...
Git gom 4 trang thai: untracked, modified, unmodified va staged.

Cac khai niem co ban:
- repository: la noi luu tru toan bo thong tin va cac phien ban chinh sua cua project.
+ co 2 loai repo la local repo va remote repo.
- branch: giup thuc hien cac task song song ma khong anh huong lan nhau, sau khi hoan thien thi merge lai vao master la xong project.
+ tao moi 1 branch va chuyen sang lam viec tai branch do: 
         git checkout -m [name_new_branch]
+ chuyen sang lam viec tai branch B:
         git checkout [name_branch]
+ Doi ten 1 branch:
         git checkout -m [name_old_branch] [name_new_branch]
- merging
- git stash
- git rebase