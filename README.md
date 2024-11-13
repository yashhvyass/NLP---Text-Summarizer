# NLP--- End to End Text-Summarizer

## Workflows

Textly
Textly is an advanced text paraphrasing web application, designed as an intelligent alternative to Quillbot. Built on the Flask framework and powered by Hugging Face’s pretrained BERT model, Textly delivers high-quality paraphrasing with a BLEU score of 45. This application provides users with a range of paraphrasing styles, enhancing both flexibility and precision in text rewriting tasks. Textly is ideal for students, writers, and professionals looking for effective ways to rephrase content while maintaining the original meaning.

## Demo
You can view a live demo of the application on Vercel.

## Features
- Paraphrasing Styles: Offers multiple styles of text paraphrasing to suit different user needs.
- High-Quality Rewrites: Utilizes Hugging Face’s BERT model to produce high-quality paraphrased content.
- Performance: Achieves a BLEU score of 45, indicating strong similarity to human paraphrasing.
- REST API: Supports integration with other applications through a FastAPI-powered RESTful API.
- Dockerized Setup: Easily deployable with Docker for consistent environment configuration.

## Technology Stack
- Transformers: Pretrained BERT model from Hugging Face for text paraphrasing.
- PyTorch: Framework used for deep learning model handling.
- Flask: Web application framework for building the front end and handling requests.
- FastAPI: Used for creating the REST API interface.
- Docker: Containerization for seamless deployment and consistent development environments.
- Vercel: Platform for deployment and hosting.
- Git: Version control for tracking and managing code changes.
- JavaScript: Enhances interactivity on the front end.

## Usage
Text Paraphrasing: Enter text in the provided input field, select a paraphrasing style, and submit.
API Access: For programmatic access, refer to the /docs endpoint for API documentation.

## Deployment
To deploy Textly on Vercel or a similar hosting platform:

1. Set up the environment variables required for your model and API.
2. Build the Docker image and push it to a container registry.
3. Link the container registry with your Vercel project for seamless deployment.

## API Documentation
- Textly includes a RESTful API built with FastAPI for easy integration with other applications. Access the API documentation at /docs once the application is running.

## Contributing
Contributions to Textly are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Submit a pull request.

## Contact
For further information or questions, please contact the project maintainer at yashhvyass@gmail.com.
