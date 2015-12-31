* cara push - pull - commit yang benar :

1. buat brach baru (misalkan namanya : develop) di project. caranya :
	a. klik kanan di project ( disini ), pilih "git bash"
	b. ketikkan perintah "git checkout -b develop"

2. aturan-aturan
	1. setiap akan melakukan coding, masuk kedalam branch master (git checkout master)
	2. lakukan pull untuk mendapatkan update (git pull)
	3. masuk kedalam brach develop (git checkout develop)
	4. lakukan coding 
	5. untuk commit, klik kanan pada project pilih git GUI
	6. pilih semua file yang berubah, dan commit
	7. masuk kedalam branch master(git checkout master)
	8. lakukan pull (git pull)
	9. lakukan perintah "git merge --no-ff nama_branch"
	10. push (git push)
	11. masuk kedalam tahap 2

3. aturan code
	1. kasih command dalam setiap fungsi yang menggunakan library (nama algo yang digunakan)
	2. buat class tiap metode
	3. nama variabel lower case dengan pemisah "_"
	4. nama class, awalan huruf besar dan chamelCase
	5. untuk function chamelCase