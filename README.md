# My FastAPI Project

This is a basic FastAPI project structure.
# Generate image with Api of getimg.ai



## Description

generate image with Api of getimg.ai


## API Documentation

### Endpoint: generate image


-   URL    : host:port/get-image

-   Method : Post

-   Request Parameters:

    - Body Parameters:
        -   prompt : Text input required to guide the image generation. (string)
        -   negative_prompt: Text input that will not guide the image generation. (string)
        -   width:  The width of the generated image in pixels,Width needs to be multiple of 64 (integer 256 to 1536)
        -   height: The height of the generated image in pixels,Height needs to be  multiple of 64 (integer 256 to 1536)


-   Response Parameters:

        - Success Response:

            -    {
                    "status":200,
                    "data":{
                        "seed":integer,
                        "cost":float,
                        "url" : image url
                    }
                }
        
        -   Bad Request:

            -   {
                "status":500,
                "message": "Failed to generate image"
            }


## Installation
1. **Clone the repository:**
   ```bash
   git clone git@github.com:xuantoan0406/ImageGen.git
   cd ImageGen

2. **Run project:**

    -   Replace the env.example file with .env

    ```bash
   docker-compose up --build

