<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center"> Project NBA Player </h3>

  <p align="center">
    Here is a project of my own, based on a classical dataset (NBA PLayers), in which I wanted to use the Logistic Regression and the adaptable threshold of a Classification Model in order to create a API and a simple Front End. This "website" will give trainers advices if a player will be playing in 5 years according to some arbitrary characteristics.
    <br />
    <a href="https://github.com/Zebho/NBA_Player_Analysis"><strong> Explore the docs </strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#the-data">The Data</a></li>
      </ul>
      <ul>
        <li><a href="#the-preprocessing">The Preprocessing</a></li>
      </ul>
      <ul>
        <li><a href="#the-models">The Models</a></li>
      </ul>
      <ul>
        <li><a href="#the-metrics">The Metrics</a></li>
      </ul>
      <ul>
        <li><a href="#improvementsh">Improvements</a></li>
      </ul>
    </li>
    <li>
      <a href="#built-with">Built With</a>
    </li>
     <li>
      <a href="#licence">Licence</a>
    </li>
     <li>
      <a href="#contacts">Contacts</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The aim of this project is to set up a prediction about a player, if he will keep playing in 5 years or not according to some arbitrary characteristics. This project is based on a classical dataset NBA Player, and help me used the classification models and the API and frontend productions.

The project therefore comprises 4 phases:
1) First of all, I carried out a search to find the best model in our case.
2) Once I'd found it, I set about improving it and modifying its threshold, to maximise its accuracy. I save both model and scaler, in order to use them in my API.
3) I then created a Docker image of the whole thing in order to use it in the form of an API, made available on GCPlateform.
4) Finally, I set up a simple Streamlit to request the API and display whether the player's statistics entered by the user can be used to bet on him or not.

The project was carried out so that I could familiarise myself with classification models and put them into an API and frontend productions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### The Data
The data comes from Kaggle Website [NBA Prediction](https://www.kaggle.com/code/yalcinberkay/nba-match-prediction-result-points).

### The Preprocessing
The preprocessing is a classic one : one checks the duplicated lines, the take care of the NaNs and split the X an Y.

We apply a MinMaxScaler before each model.

### The Models
I have chosen 4 models :
* The LogReg
* The KNN
* The SVM

### The Metrics
To compare them, I will use the f1 metrics to find which one is the best here. Then, I will use the precision and maximize it.

### Improvements
Some improvepents can be made :
* The frontend can be worked on
* The possibility to adjust the precision
* An easy way to give the caracterictics


## Built With

This section list any major frameworks/libraries used :

* SKLearn

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Arthur DUBOIS - [@zebh0](https://twitter.com/zebh0) - arthurdubsm@gmail.com

Project Link: [https://github.com/Zebho/Prediction_Consumption_French_Electricity?tab=readme-ov-file](https://github.com/Zebho/Prediction_Consumption_French_Electricity?tab=readme-ov-file)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

Thank you for your attention.
