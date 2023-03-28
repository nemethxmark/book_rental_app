# Book Rental 

Book Rental is a web-based full-stack application for managing book renting.
Users, books and rent events can be created/searched/updated and deleted (CRUD operations).

Tech stack used for the project - Python, FastAPI, JS, React
## Usage

Use [Docker](https://www.docker.com/) to run the containerized backend part of the app.

```bash
cd backend
sudo docker-compose up --build
```

Once it composed, the backend can be reached from your browser at 0.0.0.0:8000.

If the backend up and running, the frontend part can be started.
For that, [NodeJS and NPM](https://kinsta.com/blog/how-to-install-node-js/) are both need to be installed (dockerizing it is planned)

```bash
cd frontend/fronted
sudo npm start
```

## Improvement plans

- Authentication (backend is ready, frontend is in progress)
- Fronted - create a rent event in a more interactive way
- Frontend - containerizing it
- Backend - fetching available books depending on the date (currently works ony for the day of running)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


