# MRT-pet backend

### Run the application use the Docker Image
1. Create `.env` file
```
DATABASE_URL=mongodb://mongodb:27017/lms
secret_key=guiyfgc837tgf3iw87-012389764
```
2. Create `docker-compose.yml` file and paste the following
```yaml
version: "3"

services:
  backend:
    image: patri27826/mrt_pet_backend:0.0.1
    ports:
      - 8080:8080
    env_file:
      - .env

  mongodb:
    image: mongo:6.0.9
    ports:
      - 27017:27017
    volumes:
      - .data/mongodb:/data/db
```
3. Run `$ docker compose up --build` command
4. Check the Api Documentation via `http://localhost:8080/docs`


### Run the Application under repository
```console
$ docker compose up --build
```

### Before Commit
```
$ pip install pre-commit
$ pre-commit install
```

### Add the package
```console
$ poetry add {package name}
```
