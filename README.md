## Getting started with projects related to gemini-pro & gemini-pro-vision models.

## 1. A simple health app using gemini.

### Health Checker App

#### Aim of Project
The aim of this project is to build a health checker app using a generative AI model. The app allows users to input a prompt related to nutrition, upload an image containing food items, and receive a response that includes the calorie count for individual food items in the image.

#### Steps Involved
##### Setting Up Environment:
The project uses Streamlit for building the web app interface.
It integrates with the Google Generative AI API for generating responses based on user input and uploaded images.

##### Getting Model Response:
The get_gemini_repsonse function is defined to interact with the generative AI model ('gemini-pro-vision') and obtain responses based on the provided input, image, and prompt.

##### Image Processing:
The input_image_setup function processes the uploaded image file, converting it into bytes and extracting necessary information such as MIME type.

##### Streamlit Interface:
The Streamlit app interface is set up to take user input for the prompt and allow image upload.
Users can input a prompt related to food items and upload an image containing those items.

##### Response Display:
Upon clicking the "Calories count" button, the app sends the input, image, and prompt to the generative AI model and displays the response, which includes the estimated calorie count for individual food items.

#### Tools/Technologies Required
Python
Streamlit
Google Generative AI API
Pillow (PIL) for image processing
Python-dotenv for environment variable management

#### Conclusion
The health checker app provides a simple and interactive way for users to inquire about the calorie count of food items in an image. It leverages generative AI to generate responses based on the user's input and the content of the uploaded image.

#### What Extra Can Be Done in This Project

##### Enhanced Image Recognition:
Explore and implement advanced image recognition techniques to identify and classify food items more accurately.
##### Extended Nutrition Information:
Extend the app to provide additional nutritional information for each food item, such as macronutrients and micronutrients.
##### User Authentication:
Implement user authentication to personalize the experience and save the history of queries.
##### Mobile App Development:
Consider expanding the app to a mobile platform to increase accessibility.
##### Feedback Mechanism:
Incorporate a feedback mechanism to improve the model's accuracy based on user feedback.

## 2. Invoice generator app using gemini llm

### MultiLanguage Invoice Extractor

#### Aim of Project
The goal of this project is to create a MultiLanguage Invoice Extractor using generative AI. The application allows users to input a prompt related to invoice details, upload an image containing an invoice, and receive a response that includes extracted information from the invoice.

#### Steps Involved

##### Setting Up Environment:
The project uses Streamlit for building the web app interface.
It integrates with the Google Generative AI API for generating responses based on user input and uploaded invoice images.

##### Loading Gemini Pro Vision Model:
The GenAI library is used to configure and load the 'gemini-pro-vision' generative model.

##### Getting Gemini Response:
The get_gemini_response function interacts with the generative AI model to obtain responses based on the provided input, image, and user prompt.

##### Image Processing:
The input_image_details function processes the uploaded invoice image file, converting it into bytes and extracting necessary information such as MIME type.

##### Streamlit Interface:
The Streamlit app interface is set up to take user input for the prompt and allow image upload.
Users can input a prompt related to invoices and upload an image containing the invoice.

##### Response Display:
Upon clicking the "For invoice details...click here" button, the app sends the input, image, and prompt to the generative AI model and displays the response, which includes extracted details from the invoice.

#### Tools/Technologies Required
Python
Streamlit
Google Generative AI API
Pillow (PIL) for image processing
Python-dotenv for environment variable management

#### Conclusion
The MultiLanguage Invoice Extractor provides an interactive way for users to inquire about details present in an invoice image. It utilizes generative AI to generate responses based on the user's input and the content of the uploaded invoice image.

#### What Extra Can Be Done in This Project

##### Multilingual Support:
Enhance the application to support a wider range of languages for invoice details extraction.

##### Additional Invoice Details:
Extend the app to extract additional details from invoices, such as due dates, itemized lists, and payment information.

##### User Feedback Mechanism:
Implement a feedback mechanism to improve the model's accuracy based on user corrections or validations.

##### Integration with OCR Libraries:
Integrate Optical Character Recognition (OCR) libraries to improve the accuracy of text extraction from invoice images.

###### Automated Testing:
Implement automated testing to ensure the reliability of the invoice extraction functionality.