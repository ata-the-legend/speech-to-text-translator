# speech-to-text-translator

This project is a microservice-based system that provides speech-to-text transcription and translation capabilities. It consists of two services connected via RabbitMQ message queue.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Services](#services)
  - [ASR Service](#asr-service)
  - [Translator Service](#translator-service)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Running with Docker Compose](#running-with-docker-compose)
- [Usage](#usage)
  - [Transcription Endpoint](#transcription-endpoint)
  - [Translation Endpoint](#translation-endpoint)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automatic Speech Recognition (ASR) using the Vosk model
- English to Farsi translation using the Deep Translator library
- Microservice architecture with RabbitMQ message queue
- Horizontal scaling using Docker containers
- FastAPI web framework for the ASR service

## Architecture

The project follows a microservice architecture, where the ASR and Translator services communicate through a RabbitMQ message queue. This design allows for scalability and flexibility, as the services can be scaled independently based on the workload.


    A[User] --> B[ASR Service]
    B --> C[RabbitMQ]
    C --> D[Translator Service]
    D --> C
    C --> B 

## Services
### ASR Service

The ASR service is responsible for transcribing audio files (in WAV format) and sending the recognized English text to the Translator service.

#### Endpoints:

- POST /transcribe: Accepts a WAV audio file and triggers the ASR process, then sends the English text to the Translator service.

- GET /translate: Returns the translated Farsi text if it's ready, or an "In Progress" message if the translation is still being processed.


### Translator Service

The Translator service receives the English text from the ASR service, translates it to Farsi, and stores the translated text.



## Installation
### Prerequisites

- Docker
- Docker Compose

### Running with Docker Compose

1. Clone the repository:
    ```bash
    git clone git@github.com:ata-the-legend/speech-to-text-translator.git
2. Change into the project directory:

   ```
    cd speech-to-text-translator

3. Start the services using Docker Compose: 
    ```
    docker-compose up -d

This will start the ASR service, Translator service, and RabbitMQ message queue.

## Usage

### Transcription Endpoint

To transcribe an audio file and get the Farsi translation:

1. Send a POST request to the /transcribe endpoint with the WAV audio file in the request body:
    ```
    curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/path/to/audio.wav" http://localhost:8000/transcribe
    
This will trigger the ASR process and send the English text to the Translator service.

### Translation Endpoint

To retrieve the Farsi translation:

1. Send a GET request to the /translate endpoint:
    ```
    curl http://localhost:8000/translate

This will return the Farsi translation if it's ready, or an "In Progress" message if the translation is still being processed.

## Contributing

1. Fork the repository
2. Create your feature branch (git checkout -b feature/your-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin feature/your-feature)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.
