# Mario's Wine Guide - Interactive Tour of Italian Wines

An interactive map that helps you discover Italian wines and spirits. Click on any region of Italy, and Mario (our AI wine expert) will tell you all about the local specialties!

## Requirements
- **Docker** and **Docker Compose** installed on your system
- **GPU support** for optimal performance
- If you don't have GPU support, make sure **Docker** has access to at least **16GB of free RAM**

## Quick Start
### 1. Clone the repository:
```sh
git clone https://github.com/ginstrom/mario_wine_guide.git
cd mario_wine_guide
```

### 2. Start the application:
```sh
docker-compose up --build
```
> **Note:** The first startup may take several minutes as it downloads and sets up the AI model.

### 3. Open in your browser:
Visit: [http://localhost:5000](http://localhost:5000)

## How to Use
1. Wait for the application to fully start (you'll see a map of Italy).
2. Click on any region you're interested in.
3. Mario will tell you about the wines and spirits from that region.
4. Click outside the map or on the logo to return to the main view.

## Troubleshooting
If the application doesn't start:
- Ensure **ports 5000 and 11434** are available on your system.
- Try stopping and restarting:
  ```sh
  docker-compose down
  docker-compose up --build
  ```

## License
**MIT License** - Feel free to use and modify as needed.
