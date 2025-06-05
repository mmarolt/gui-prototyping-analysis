from langchain.prompts import PromptTemplate

#instruction
SUMMARY2CODE_ZS = PromptTemplate(
    input_variables=["summary"],
    template=
"""Given a short description of a mobile page, implement the described page with HTML and inline CSS code: 
{summary}
Make sure, that the mobile page displays well in the Google Chrome Developer Tools when simulating a device with a mobile screen size of 375 x 667 pixels.
"""
)

#PD_ZS
SUMMARY2REQUIREMENTS_ZS = PromptTemplate(
    input_variables=["summary"],
    template= """Using the provided short description of a mobile page, please analyze the content and identify the specific features that are necessary for optimal functionality and user experience. Focus solely on visible functionalities: {summary}"""
)
REQUIREMENTS2IMPLEMENTATION_ZS = PromptTemplate(
    input_variables=["requirements"],
    template="Describe the necessary UI elements, for implementing a mobile page with the following features: {requirements}"
)
IMPLEMETATION2STRUCTURE_ZS = PromptTemplate(
    input_variables=["implementation"],
    template="Given a List of UI Elements for a mobile page. How could this page be structured: {implementation}"
)
STRUCTURE2CODE_ZS = PromptTemplate(
    input_variables=["structure"],
    template=
"""
Given a Structure of UI Elements for a mobile page. Implement the described page with HTML and inline CSS code:
{structure}
Make sure, that the mobile page displays well in the Google Chrome Developer Tools when simulating a device with a mobile screen size of 375 x 667 pixels.
"""
)

#PD_FS
SUMMARY2REQUIRMENTS_FS = PromptTemplate(
    input_variables=["summary"],
    template= 
"""
Q:

Using the provided short description of a mobile page, please analyze the content and identify the specific features that are necessary for optimal functionality and user experience. Focus solely on visible functionalities:

A page from a language learning app, presenting a sentence translation task.

A:

1. Clear Task Presentation: The task “Translate this sentence” should be prominent, as well as the sentence, the user needs to translate.
2. User Input: The user should be able to type in his translation for the sentence.
3. Audio Functionality: ****The user should be able to listen to the sentence, which is essential for learning pronunciation and listening skills.
4. Progress Indicator: A progress bar or indicator provides feedback on the user's progression through the lesson or activity.
5. Control: Allow the user to either skip the current sentence or submit and check the translation they have entered.

Q:

Using the provided short description of a mobile page, please analyze the content and identify the specific features that are necessary for optimal functionality and user experience. Focus solely on visible functionalities:

A page from an e-commerce app, presenting a list of armchairs to buy.

A:

1. Heading: The page should prominently display, that it is dedicated to “armchairs”
2. Product List: The user should be able to scroll through a List of different armchairs
3. Product Display: Each armchair is represented by an image, allowing users to visually identify the product.
4. Product Information: For each product, the category, the name and the price is displayed
5. Navigation Controls: The user should be able to return to the previous screen.
6. Filter Option: The user can access a filter option, for narrowing down their search based on certain criteria.
7. Shopping List: The user should be able to open a shopping list to view selected items. The amount of products on currently displayed should also be provided.

Q:

Using the provided short description of a mobile page, please analyze the content and identify the specific features that are necessary for optimal functionality and user experience. Focus solely on visible functionalities:

{summary}

A:
"""
)
REQUIREMENTS2IMPLEMENTATION_FS = PromptTemplate(
    input_variables=["requirements"],
    template=
"""
Q:

Describe the necessary UI elements, for implementing a mobile page with the following features:

1. Clear Task Presentation: The task “Translate this sentence” should be prominent, as well as the sentence, the user needs to translate.
2. User Input: The user should be able to type in his translation for the sentence.
3. Audio Functionality: ****The user should be able to listen to the sentence, which is essential for learning pronunciation and listening skills.
4. Progress Indicator: A progress bar or indicator provides feedback on the user's progression through the lesson or activity.
5. Control: Allow the user to either skip the current sentence or submit and check the translation they have entered.

A:

1. Clear Task Presentation:
    - Task Description Display: A simple Text Label, that shows the task for the user: “Translate this sentence”
    - Text Sentence Display: A simple Text Label, that displays the sentence, that needs to be translated. e.g.: “mis animales, mi tortuga, mi cangrejo.”
2. User Input:
    - Translation Input Field: A text area, with a placeholder that says “Type the English translation”, where the user can type in his translation.
3. Audio Functionality:
    - Pronunciation Button: A Speaker icon, the user can click on, to listen to the pronunciation of the given sentence.
4. Progress Indicator: 
    - Progress Bar: A progress bar, that displays the user’s progression through the lesson.
5. Control: 
    - Skip Button: A button with the label “Skip” allows the user to skip the current sentence
    - Check Button: A button with the label “check” allows the user to submit and verify their translation

Q:

Describe the necessary UI elements, for implementing a mobile page with the following features:

1. Heading: The page should prominently display, that it is dedicated to “armchairs”
2. Product List: The user should be able to scroll through a List of different armchairs
3. Product Display: Each armchair is represented by an image, allowing users to visually identify the product.
4. Product Information: For each product, the category, the name and the price is displayed
5. Navigation Controls: The user should be able to return to a previous screen.
6. Filter Option: The user can access a filter option, for narrowing down their search based on certain criteria.
7. Shopping List: The user should be able to open a shopping list to view selected items. The amount of products on currently displayed should also be provided.

A:

1. Heading:
    - Category display: A Text label that says “armchairs”
2. Product List:
    - Scrollable container: A vertical scroll view, that allows the user to scroll through the List of armchairs
3. Product Display:
    - Image Thumbnails: Image containers to display thumbnails of each armchair product.
4. Product Information:
    - Product Information displays: Text Labels for displaying the product category, name, and price of each product
5. Navigation Controls:
    - Back Button: Include a back button in the form of an arrow pointing to the left, to allow users to return to the previous screen.
6. Filter Option:
    - Filter Button: A filter button, to indicate where users can access filters.
7. Shopping List:
    - Shopping List Button: A clickable section, that the user can tap to open the shopping List.
    - Badge with Item Count: a small badge indicating the number of items in the user’s shopping list.

Q:

Describe the necessary UI elements, for implementing a mobile page with the following features:

{requirements}

A:
"""
)
IMPLEMETATION2STRUCTURE_FS = PromptTemplate(
    input_variables=["implementation"],
    template=
"""
Q:

Given a List of UI Elements for a mobile page. How could this page be structured:

1. Clear Task Presentation:
    - Task Description Display: A simple Text Label, that shows the task for the user: “Translate this sentence”
    - Text Sentence Display: A simple Text Label, that displays the sentence, that needs to be translated. e.g.: “mis animales, mi tortuga, mi cangrejo.”
2. User Input:
    - Translation Input Field: A text area, with a placeholder that says “Type the English translation”, where the user can type in his translation.
3. Audio Functionality:
    - Pronunciation Button: A Speaker icon, the user can click on, to listen to the pronunciation of the given sentence.
4. Progress Indicator: 
    - Progress Bar: A progress bar, that displays the user’s progression through the lesson.
5. Control: 
    - Skip Button: A button with the label “Skip” allows the user to skip the current sentence
    - Check Button: A button with the label “check” allows the user to submit and verify their translation

A:

1. Top Section:
    - Task Description Display: A simple Text Label, that shows the task for the user: “Translate this sentence”
        - Place this at the very top of the page. It should be prominent, immediately informing the user of the task.
    - Text Sentence Display: A simple Text Label that displays the sentence that needs to be translated. e.g.: “mis animales, mi tortuga, mi cangrejo.”
        - Place immediately below the task description.
    - Pronunciation Button: A Speaker icon, the user can click on, to listen to the pronunciation of the given sentence.
        - Place it near the sentence display, possibly to the left of it.
    - Progress Bar: A progress bar, that displays the user’s progression through the lesson.
        - Position it at the very top, even above the task description
2. Middle Section:
    - Translation Input Field: A text area, with a placeholder that says “Type the English translation”, where the user can type in his translation.
        - This should be centrally located on the page, just below the sentence display. The input field should be large enough to accommodate longer sentences.
3. Bottom Section:
    - Skip Button: A button with the label “Skip” allows the user to skip the current sentence
        - Place this button on the lower left side of the screen.
    - Check Button: A button with the label “check” allows the user to submit and verify their translation
        - This should be on the lower right side, mirroring the skip button.
    - The Skip Button should be a lot smaller in widht compared to the check button, making the check button much more prominent than the skip button.

Q:

Given a List of UI Elements for a mobile page. How could this page be structured:

1. Heading:
    - Category display: A Text label that says “armchairs”
2. Product List:
    - Scrollable container: A vertical scroll view, that allows the user to scroll through the List of armchairs
3. Product Display:
    - Image Thumbnails: Image containers to display thumbnails of each armchair product.
4. Product Information:
    - Product Information displays: Text Labels for displaying the product category, name, and price of each product
5. Navigation Controls:
    - Back Button: Include a back button in the form of an arrow pointing to the left, to allow users to return to the previous screen.
6. Filter Option:
    - Filter Button: A filter button, to indicate where users can access filters.
7. Shopping List:
    - Shopping List Button: A clickable section, that the user can tap to open the shopping List.
    - Badge with Item Count: a small badge indicating the number of items in the user’s shopping list.

A:

1. Header
    - Back Button: Include a back button in the form of an arrow pointing to the left, to allow users to return to the previous screen.
        - Should be placed in the upper left corner of the screen
    - Filter Button: A filter button, to indicate where users can access filters.
        - Should be placed in the upper right corner of the screen
    - Category Display: A Text label that says “armchairs”
        - should be placed in the middle of the header section, between back arrow and filter button
2. Scrollable container: A vertical scroll view should be present in the middle of the screen, that allows the user to scroll through the List of armchairs. Each Item on the list should contain:
    - Image Thumbnails: Image containers to display thumbnails of each armchair product.
        - should be placed on the Left side
    - Product Information displays: Text Labels for displaying the product category, name, and price of each product
        - The three labels should be right to the Image. with the the product category on top, following the name and at the bottom the price.
    - For demo purposes, three examples should be provided
        - Chair, EKERÖ, $149.00
        - Chair, JÄPPLING, $169.00
        - Rocking chair, IKEA PS GULLHOLMEN $69.99
3. Shopping List Button: A clickable section representing the bottom section of the page, that the user can tap to open the shopping List.
    - Badge with Item Count: a small badge indicating the number of items in the user’s shopping list.
        - should be placed inside the clickable section, in the lower left corner of the screen.

Q:

Given a List of UI Elements for a mobile page. How could this page be structured:

{implementation}

A:
"""
)
STRUCTURE2CODE_FS = PromptTemplate(
    input_variables=["structure"],
    template=
"""
Q:

Given a Structure of UI Elements for a mobile page. Implement the described page with HTML and inline CSS code:

1. Top Section:
    - Task Description Display: A simple Text Label, that shows the task for the user: “Translate this sentence”
        - Place this at the very top of the page. It should be prominent, immediately informing the user of the task.
    - Text Sentence Display: A simple Text Label that displays the sentence that needs to be translated. e.g.: “mis animales, mi tortuga, mi cangrejo.”
        - Place immediately below the task description.
    - Pronunciation Button: A Speaker icon, the user can click on, to listen to the pronunciation of the given sentence.
        - Place it near the sentence display, possibly to the left of it.
    - Progress Bar: A progress bar, that displays the user’s progression through the lesson.
        - Position it at the very top, even above the task description
2. Middle Section:
    - Translation Input Field: A text area, with a placeholder that says “Type the English translation”, where the user can type in his translation.
        - This should be centrally located on the page, just below the sentence display. The input field should be large enough to accommodate longer sentences.
3. Bottom Section:
    - Skip Button: A button with the label “Skip” allows the user to skip the current sentence
        - Place this button on the lower left side of the screen.
    - Check Button: A button with the label “check” allows the user to submit and verify their translation
        - This should be on the lower right side, mirroring the skip button.
    - The Skip Button should be a lot smaller in widht compared to the check button, making the check button much more prominent than the skip button.

Make sure, that the mobile screen displays well in the Google Chrome Developer Tools when simulating a device with a mobile screen size of 375 x 667 pixels.

A:

<!DOCTYPE html>
<html>
<head>
    <title>Translation Exercise</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            height: 100vh;
            background-color: #f4f4f4;
        }}
        .progress-bar {{
            height: 1vh;
            background-color: #e0e0e0;
            border-radius: 10px;
            margin: 1vh 5%;
            width: 90%;
        }}
        .progress {{
            height: 100%;
            width: 50%;
            background-color: #4caf50;
            border-radius: 10px;
            text-align: center;
            line-height: 1vh;
            color: white;
        }}
        .task-description {{
            margin: 2vh 0;
            font-size: 5vw;
            font-weight: bold;
        }}
        .sentence {{
            margin: 0vh 0;
            font-size: 4vw;
        }}
        .input-section {{
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin: 0 5%;
        }}
        textarea {{
            width: calc(100% - 4vw);
            margin: 3vh 0;
            padding: 2vh 2vw;
            height: calc(100%);
            resize: none;
            font-size: 3.5vw;
            border: 1px solid #ccc;
            border-radius: 5px;
        }}
        .control-buttons {{
            display: flex;
            justify-content: space-between;
            margin: 2vh 5%;
        }}

        button.skip {{
            flex-basis: 20%;
            padding: 1.5vh 0;
            font-size: 4vw;
            border-radius: 5px;
            border: none;
            background-color: #4caf50;
            color: white;
        }}

        button.check {{
            flex-basis: 70%;
            padding: 1.5vh 0;
            font-size: 4vw;
            border-radius: 5px;
            border: none;
            background-color: #4caf50;
            color: white;
        }}
        .speaker-icon {{
            border: none;
            background-color: transparent;
            font-size: 6vw;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <div class="progress-bar">
        <div class="progress">50%</div>
    </div>
    <div class="task-description">Translate this sentence</div>
    <div class="sentence">
      <button class="speaker-icon">&#x1F50A;</button>
      mis animales, mi tortuga, mi cangrejo. 
    </div>
    <div class="input-section">
        <textarea placeholder="Type the English translation"></textarea>
    </div>
    <div class="control-buttons">
        <button class="skip">Skip</button>
        <button class="check">Check</button>
    </div>
</body>
</html>

Q:

Given a Structure of UI Elements for a mobile page. Implement the described page with HTML and inline CSS code:

1. Header
    - Back Button: Include a back button in the form of an arrow pointing to the left, to allow users to return to the previous screen.
        - Should be placed in the upper left corner of the screen
    - Filter Button: A filter button, to indicate where users can access filters.
        - Should be placed in the upper right corner of the screen
    - Category Display: A Text label that says “armchairs”
        - should be placed in the middle of the header section, between back arrow and filter button
2. Scrollable container: A vertical scroll view should be present in the middle of the screen, that allows the user to scroll through the List of armchairs. Each Item on the list should contain:
    - Image Thumbnails: Image containers to display thumbnails of each armchair product.
        - should be placed on the Left side
    - Product Information displays: Text Labels for displaying the product category, name, and price of each product
        - The three labels should be right to the Image. with the the product category on top, following the name and at the bottom the price.
    - For demo purposes, three examples should be provided
        - Chair, EKERÖ, $149.00
        - Chair, JÄPPLING, $169.00
        - Rocking chair, IKEA PS GULLHOLMEN $69.99
3. Shopping List Button: A clickable section representing the bottom section of the page, that the user can tap to open the shopping List.
    - Badge with Item Count: a small badge indicating the number of items in the user’s shopping list.
        - should be placed inside the clickable section, in the lower left corner of the screen.

Make sure, that the mobile screen displays well in the Google Chrome Developer Tools when simulating a device with a mobile screen size of 375 x 667 pixels.

A:

<!DOCTYPE html>
<html>
<head>
    <title>Armchair Catalog</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f0f0f0;
            width: 375px;
            max-width: 100%;
            overflow-x: hidden;
        }}
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #f8f8f8;
            padding: 10px 15px;
            box-sizing: border-box;
        }}
        .header > * {{
            flex: 1;
            text-align: center;
        }}
        .header > :first-child {{
            text-align: left;
        }}
        .header > :last-child {{
            text-align: right;
        }}
        .scrollable-container {{
            overflow-y: auto;
            padding: 10px;
            box-sizing: border-box;
            height: calc(100vh - 160px);
        }}
        .product {{
            background: #fff;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 10px;
            box-sizing: border-box;
        }}
        .product img {{
            width: 80px;
            height: 80px;
            margin-right: 10px;
        }}
        .product-info {{
            display: flex;
            flex-direction: column;
        }}
        .shopping-list-button {{
            position: fixed;
            bottom: 0;
            width: 375px;
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 15px;
            box-sizing: border-box;
        }}
        .badge {{
            display: inline-block;
            background-color: red;
            color: white;
            border-radius: 50%;
            padding: 2px 8px;
            font-size: 14px;
            position: absolute;
            left: 20px;
            bottom: 18px;
        }}
        .back-button {{
            font-size: 24px;
            border: none;
            background: none;
            cursor: pointer;
        }}
        .filter-button {{
            border: none;
            background: none;
            cursor: pointer;
            font-size: 16px;
        }}
    </style>
</head>
<body>

<div class="header">
    <button class="back-button">&lt;</button>
    <span>Armchairs</span>
    <button class="filter-button">Filter</button>
</div>

<div class="scrollable-container">
    <div class="product">
        <img src="path_to_chair_image.jpg" alt="Chair Image">
        <div class="product-info">
            <span>Chair</span>
            <span>EKERÖ</span>
            <span>$149.00</span>
        </div>
    </div>
    <div class="product">
        <img src="path_to_chair_image.jpg" alt="Chair Image">
        <div class="product-info">
            <span>Chair</span>
            <span>JÄPPLING</span>
            <span>$169.00</span>
        </div>
    </div>
    <div class="product">
        <img src="path_to_chair_image.jpg" alt="Chair Image">
        <div class="product-info">
            <span>Rocking chair</span>
            <span>IKEA PS GULLHOLMEN</span>
            <span>$69.99</span>
        </div>
    </div>
</div>

<div class="shopping-list-button">
    Shopping List
    <span class="badge">3</span>
</div>

</body>
</html>

Q: 

Given a Structure of UI Elements for a mobile page. Implement the described page with HTML and inline CSS code:

{structure}

Make sure, that the mobile screen displays well in the Google Chrome Developer Tools when simulating a device with a mobile screen size of 375 x 667 pixels.

A:
"""
)

#CoT_ZS
CoT_ZS = PromptTemplate(
    input_variables=["summary"],
    template=
"""
Based on a short description, create a mobile page, by completing the following steps:

1. Using the provided short description of a mobile page, please analyze the content and identify the specific features that are necessary for optimal functionality and user experience. Focus solely on visible functionalities
2. Describe the necessary UI elements, for implementing a mobile page with the features, identified in the first step.
3. How could the UI Elements be structured into a mobile page?
4. Develop the mobile page using HTML, and inline CSS styling. Make sure, that the mobile page displays well in the Google Chrome Developer Tools when simulating a device with a mobile screen size of 375 x 667 pixels.

{summary}
"""

)

#CoT_FS
CoT_FS = PromptTemplate(
    input_variables=["summary"],
    template=
"""
Q:
Based on a short description, create a mobile page, by following these steps:

1. Using the provided short description of a mobile page, please analyze the content and identify the specific features that are necessary for optimal functionality and user experience. Focus solely on visible functionalities
2. Describe the necessary UI elements, for implementing a mobile page with the features, identified in the first step.
3. How could the UI Elements be structured into a mobile page?
4. Develop the mobile page using HTML, and inline CSS styling. Make sure, that the mobile page displays well in the Google Chrome Developer Tools when simulating a device with a mobile screen size of 375 x 667 pixels.

The mobile screen is part of a language translator application that asks the user to translate a given text sentence.

A:

Feature list:

1. Clear Task Presentation: The task “Translate this sentence” should be prominent, as well as the sentence, the user needs to translate.
2. User Input: The user should be able to type in his translation for the sentence.
3. Audio Functionality: ****The user should be able to listen to the sentence, which is essential for learning pronunciation and listening skills.
4. Progress Indicator: A progress bar or indicator provides feedback on the user's progression through the lesson or activity.
5. Control: Allow the user to either skip the current sentence or submit and check the translation they have entered.

UI Elements:

1. Clear Task Presentation:
    - Task Description Display: A simple Text Label, that shows the task for the user: “Translate this sentence”
    - Text Sentence Display: A simple Text Label, that displays the sentence, that needs to be translated. e.g.: “mis animales, mi tortuga, mi cangrejo.”
2. User Input:
    - Translation Input Field: A text area, with a placeholder that says “Type the English translation”, where the user can type in his translation.
3. Audio Functionality:
    - Pronunciation Button: A Speaker icon, the user can click on, to listen to the pronunciation of the given sentence.
4. Progress Indicator: 
    - Progress Bar: A progress bar, that displays the user’s progression through the lesson.
5. Control: 
    - Skip Button: A button with the label “Skip” allows the user to skip the current sentence
    - Check Button: A button with the label “check” allows the user to submit and verify their translation

Page structure:

1. Top Section:
    - Task Description Display: A simple Text Label, that shows the task for the user: “Translate this sentence”
        - Place this at the very top of the page. It should be prominent, immediately informing the user of the task.
    - Text Sentence Display: A simple Text Label that displays the sentence that needs to be translated. e.g.: “mis animales, mi tortuga, mi cangrejo.”
        - Place immediately below the task description.
    - Pronunciation Button: A Speaker icon, the user can click on, to listen to the pronunciation of the given sentence.
        - Place it near the sentence display, possibly to the left of it.
    - Progress Bar: A progress bar, that displays the user’s progression through the lesson.
        - Position it at the very top, even above the task description
2. Middle Section:
    - Translation Input Field: A text area, with a placeholder that says “Type the English translation”, where the user can type in his translation.
        - This should be centrally located on the page, just below the sentence display. The input field should be large enough to accommodate longer sentences.
3. Bottom Section:
    - Skip Button: A button with the label “Skip” allows the user to skip the current sentence
        - Place this button on the lower left side of the screen.
    - Check Button: A button with the label “check” allows the user to submit and verify their translation
        - This should be on the lower right side, mirroring the skip button.
    - The Skip Button should be a lot smaller in widht compared to the check button, making the check button much more prominent than the skip button.

code:

<!DOCTYPE html>
<html>
<head>
    <title>Translation Exercise</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            height: 100vh;
            background-color: #f4f4f4;
        }}
        .progress-bar {{
            height: 1vh;
            background-color: #e0e0e0;
            border-radius: 10px;
            margin: 1vh 5%;
            width: 90%;
        }}
        .progress {{
            height: 100%;
            width: 50%;
            background-color: #4caf50;
            border-radius: 10px;
            text-align: center;
            line-height: 1vh;
            color: white;
        }}
        .task-description {{
            margin: 2vh 0;
            font-size: 5vw;
            font-weight: bold;
        }}
        .sentence {{
            margin: 0vh 0;
            font-size: 4vw;
        }}
        .input-section {{
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin: 0 5%;
        }}
        textarea {{
            width: calc(100% - 4vw);
            margin: 3vh 0;
            padding: 2vh 2vw;
            height: calc(100%);
            resize: none;
            font-size: 3.5vw;
            border: 1px solid #ccc;
            border-radius: 5px;
        }}
        .control-buttons {{
            display: flex;
            justify-content: space-between;
            margin: 2vh 5%;
        }}

        button.skip {{
            flex-basis: 20%;
            padding: 1.5vh 0;
            font-size: 4vw;
            border-radius: 5px;
            border: none;
            background-color: #4caf50;
            color: white;
        }}

        button.check {{
            flex-basis: 70%;
            padding: 1.5vh 0;
            font-size: 4vw;
            border-radius: 5px;
            border: none;
            background-color: #4caf50;
            color: white;
        }}
        .speaker-icon {{
            border: none;
            background-color: transparent;
            font-size: 6vw;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <div class="progress-bar">
        <div class="progress">50%</div>
    </div>
    <div class="task-description">Translate this sentence</div>
    <div class="sentence">
      <button class="speaker-icon">&#x1F50A;</button>
      mis animales, mi tortuga, mi cangrejo. 
    </div>
    <div class="input-section">
        <textarea placeholder="Type the English translation"></textarea>
    </div>
    <div class="control-buttons">
        <button class="skip">Skip</button>
        <button class="check">Check</button>
    </div>
</body>
</html>

Q:

Based on a short description, create a mobile page, by following these steps:

1. Using the provided short description of a mobile page, please analyze the content and identify the specific features that are necessary for optimal functionality and user experience. Focus solely on visible functionalities
2. Describe the necessary UI elements, for implementing a mobile page with the features, identified in the first step.
3. How could the UI Elements be structured into a mobile page?
4. Develop the mobile page using HTML, and inline CSS styling. Make sure, that the mobile page displays well in the Google Chrome Developer Tools when simulating a device with a mobile screen size of 375 x 667 pixels.

The screen displays a List with information about upcoming Box office movies.

A:

Feature list:

1. Heading: The page should prominently display, that it is dedicated to “armchairs”
2. Product List: The user should be able to scroll through a List of different armchairs
3. Product Display: Each armchair is represented by an image, allowing users to visually identify the product.
4. Product Information: For each product, the category, the name and the price is displayed
5. Navigation Controls: The user should be able to return to a previous screen.
6. Filter Option: The user can access a filter option, for narrowing down their search based on certain criteria.
7. Shopping List: The user should be able to open a shopping list to view selected items. The amount of products on currently displayed should also be provided.

UI Elements:

1. Heading:
    - Category display: A Text label that says “armchairs”
2. Product List:
    - Scrollable container: A vertical scroll view, that allows the user to scroll through the List of armchairs
3. Product Display:
    - Image Thumbnails: Image containers to display thumbnails of each armchair product.
4. Product Information:
    - Product Information displays: Text Labels for displaying the product category, name, and price of each product
5. Navigation Controls:
    - Back Button: Include a back button in the form of an arrow pointing to the left, to allow users to return to the previous screen.
6. Filter Option:
    - Filter Button: A filter button, to indicate where users can access filters.
7. Shopping List:
    - Shopping List Button: A clickable section, that the user can tap to open the shopping List.
    - Badge with Item Count: a small badge indicating the number of items in the user’s shopping list.

Page structure:

1. Header
    - Back Button: Include a back button in the form of an arrow pointing to the left, to allow users to return to the previous screen.
        - Should be placed in the upper left corner of the screen
    - Filter Button: A filter button, to indicate where users can access filters.
        - Should be placed in the upper right corner of the screen
    - Category Display: A Text label that says “armchairs”
        - should be placed in the middle of the header section, between back arrow and filter button
2. Scrollable container: A vertical scroll view should be present in the middle of the screen, that allows the user to scroll through the List of armchairs. Each Item on the list should contain:
    - Image Thumbnails: Image containers to display thumbnails of each armchair product.
        - should be placed on the Left side
    - Product Information displays: Text Labels for displaying the product category, name, and price of each product
        - The three labels should be right to the Image. with the the product category on top, following the name and at the bottom the price.
    - For demo purposes, three examples should be provided
        - Chair, EKERÖ, $149.00
        - Chair, JÄPPLING, $169.00
        - Rocking chair, IKEA PS GULLHOLMEN $69.99
3. Shopping List Button: A clickable section representing the bottom section of the page, that the user can tap to open the shopping List.
    - Badge with Item Count: a small badge indicating the number of items in the user’s shopping list.
        - should be placed inside the clickable section, in the lower left corner of the screen.

code:

<!DOCTYPE html>
<html>
<head>
    <title>Armchair Catalog</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f0f0f0;
            width: 375px;
            max-width: 100%;
            overflow-x: hidden;
        }}
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #f8f8f8;
            padding: 10px 15px;
            box-sizing: border-box;
        }}
        .header > * {{
            flex: 1;
            text-align: center;
        }}
        .header > :first-child {{
            text-align: left;
        }}
        .header > :last-child {{
            text-align: right;
        }}
        .scrollable-container {{
            overflow-y: auto;
            padding: 10px;
            box-sizing: border-box;
            height: calc(100vh - 160px);
        }}
        .product {{
            background: #fff;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 10px;
            box-sizing: border-box;
        }}
        .product img {{
            width: 80px;
            height: 80px;
            margin-right: 10px;
        }}
        .product-info {{
            display: flex;
            flex-direction: column;
        }}
        .shopping-list-button {{
            position: fixed;
            bottom: 0;
            width: 375px;
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 15px;
            box-sizing: border-box;
        }}
        .badge {{
            display: inline-block;
            background-color: red;
            color: white;
            border-radius: 50%;
            padding: 2px 8px;
            font-size: 14px;
            position: absolute;
            left: 20px;
            bottom: 18px;
        }}
        .back-button {{
            font-size: 24px;
            border: none;
            background: none;
            cursor: pointer;
        }}
        .filter-button {{
            border: none;
            background: none;
            cursor: pointer;
            font-size: 16px;
        }}
    </style>
</head>
<body>

<div class="header">
    <button class="back-button">&lt;</button>
    <span>Armchairs</span>
    <button class="filter-button">Filter</button>
</div>

<div class="scrollable-container">
    <div class="product">
        <img src="path_to_chair_image.jpg" alt="Chair Image">
        <div class="product-info">
            <span>Chair</span>
            <span>EKERÖ</span>
            <span>$149.00</span>
        </div>
    </div>
    <div class="product">
        <img src="path_to_chair_image.jpg" alt="Chair Image">
        <div class="product-info">
            <span>Chair</span>
            <span>JÄPPLING</span>
            <span>$169.00</span>
        </div>
    </div>
    <div class="product">
        <img src="path_to_chair_image.jpg" alt="Chair Image">
        <div class="product-info">
            <span>Rocking chair</span>
            <span>IKEA PS GULLHOLMEN</span>
            <span>$69.99</span>
        </div>
    </div>
</div>

<div class="shopping-list-button">
    Shopping List
    <span class="badge">3</span>
</div>

</body>
</html>

Q:

Based on a short description, create a mobile page, by following these steps:

1. Using the provided short description of a mobile page, please analyze the content and identify the specific features that are necessary for optimal functionality and user experience. Focus solely on visible functionalities
2. Describe the necessary UI elements, for implementing a mobile page with the features, identified in the first step.
3. How could the UI Elements be structured into a mobile page?
4. Develop the mobile page using HTML, and inline CSS styling. Make sure, that the mobile page displays well in the Google Chrome Developer Tools when simulating a device with a mobile screen size of 375 x 667 pixels.

{summary}

A:
"""
)
