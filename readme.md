# Project Title

Pacmann Backend

## Description

Aplikasi backend sebagai service untuk jembatan ke database dalam proses menambah user, login user, menambah/menghapus/mengubah data dan status todo.
Aplikasi terkait adalah Pacmann Frontend yang dapat dilihat di link berikut : https://github.com/VictorSilalahi/pacmann-frontend

## Getting Started

### Dependencies

* alembic==1.10.3
* aniso8601==9.0.1
* certifi==2022.12.7
* charset-normalizer==3.1.0
* click==8.1.3
* colorama==0.4.6
* exceptiongroup==1.1.1
* Flask==2.2.3
* Flask-Cors==3.0.10
* Flask-JWT-Extended==4.4.4
* Flask-Migrate==4.0.4
* Flask-RESTful==0.3.9
* Flask-SQLAlchemy==3.0.3
* greenlet==2.0.2
* idna==3.4
* iniconfig==2.0.0
* itsdangerous==2.1.2
* Jinja2==3.1.2
* loguru==0.6.0
* Mako==1.2.4
* MarkupSafe==2.1.2
* packaging==23.0
* pluggy==1.0.0
* psycopg2==2.9.6
* PyJWT==2.6.0
* pytest==7.3.0
* python-dotenv==1.0.0
* pytz==2023.3
* requests==2.28.2
* requests-mock==1.10.0
* six==1.16.0
* SQLAlchemy==2.0.8
* swagger-gen==0.1.2
* tomli==2.0.1
* typing_extensions==4.5.0
* urllib3==1.26.15
* waitress==2.1.2
* Werkzeug==2.2.3
* win32-setctime==1.1.0



### Executing program

* Setelah seluruh file ini di clone, masuk lah ke dalam folder aplikasi ini
* jalankan beberapa command sbb: 
```
python -m venv venv
.\venv\scripts\activate
pip install -r requirements.txt
python run.py
```

## Daftar Folder dan File

* run.py ---> file utama untuk menjalankan aplikasi
* app\logs ---> folder log pencatatan error yang terjadi pada saat aplikasi berjalan
* app\utils ---> folder untuk koneksi ke database dan pengaturan logger
* app\models ---> folder untuk menyimpan skema tabel dalam database, tabel-tabel tersebut dapat dilihat di todo.py dan user.py
* app\routes ---> folder untuk konfigurasi routing endpoint, seluruh link endpoint dapat dilihat di file todo.py, todostatus.py, user.py dan users.py
* db ---> folder untuk menyimpan backup database postgresql
* migrations ---> folder yang digunakan untuk melakukan migrasi database menggunakan alembic
* test ---> folder untuk script unittest endpoint menggunakan pytest


## Authors

Victor Silalahi 
https://www.linkedin.com/in/victor-silalahi-64512211a