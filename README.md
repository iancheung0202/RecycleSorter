# RecycleSorter
RecycleSorter is a web application that automatically sorts materials based on real-time camera footage and determines if that material is recyclable. It also comes with a Discord bot extension, ReCyclists, that serves the same purpose but with images being passed to the algorithm instead of real-time camera snapshots.

_Developed for [GunnHacks 9.0](https://gunnhacks.com)_
_Awarded **Most Creative** project_

## Demo
Head over to the [demo](https://iancheung0202.github.io/RecycleSorter/) to try it out (A mobile device is recommended, though Desktop is also supported).<br>
Invite our extension Discord bot [here](https://discord.com/api/oauth2/authorize?client_id=1057333274449547354&permissions=51200&scope=bot).

## Inspiration

Sorting trash into their respective categories is an important part of proper waste disposal, yet it is often seen as an arduous and tedious task. This can lead to people not bothering to sort their trash, instead choosing to just throw them into the nearest bin. This can lead to contamination of the waste stream since recyclable materials end up in landfills and vice versa. Furthermore, it can lead to an increase in waste management costs as sorting and recycling facilities have to deal with the increase in unsorted waste. It is therefore important to make sure that people are made more aware of the importance of sorting their trash so that it can be disposed of correctly.

## What it does

RecycleSorter is a web application that utilizes real-time camera footage to automatically sort materials and determine if they are recyclable. The application utilizes a combination of computer vision and machine learning algorithms to detect and classify different types of waste material. It can detect common items such as plastic bottles, paper, aluminum cans, glass, and batteries, which it then provides detailed information regarding their respective categories. This allows users to identify any non-recyclable materials before they are mistakenly disposed of. RecycleSorter also features an easy-to-use user interface, so that users can easily manage their waste.

## How we built it

This web application is built using HTML, CSS, and JavaScript from scratch. We trained our material classification algorithms using Google Teachable Machine. A webcam is implemented into the website, taking live snapshots of the materials in question. The web application is also designed with sufficient accessibility, meaning it is mobile-friendly. The IDE for this application is Visual Studio Code and the web application is uploaded to [GitHub Pages](https://iancheung0202.github.io/RecycleSorter/) for demo.

In addition, we have built an extension Discord bot of this web application using Python, which means that users can directly upload photos on Discord, a real-time web chat platform, to obtain the classification of the item in the image. We built this bot using Replit and it is hosted 24/7. The code is also automatically deployed to the [same GitHub repo](https://github.com/iancheung0202/RecycleSorter/tree/main/ReCyclists) just for judges' reference.

## Challenges we ran into

One of the challenges we ran into when attempting to train the data was the tedious process involved. This process requires careful preparation of the data, which can be time-consuming and require a significant amount of manual effort. Additionally, once the data is ready, it must be fed into the training model and fine-tuned until the desired results are achieved. This process is often iterative, meaning each iteration requires further tweaking and refinement. This can be a laborious and time-consuming process, but one that is necessary in order to ensure accurate results.

In addition, we ran into countless errors while working on this project, ranging from minor bugs to major errors. Despite the difficulty and the time it took, we persevered and eventually solved them one by one by carefully debugging and finding the source of the problem. We kept a positive attitude throughout the process and finally developed a greater understanding of the technology we were using and the project itself, which will be invaluable in the future. 

## Accomplishments that we're proud of and what we learned

We are very proud of completing our first-ever image classification project from scratch. This 24-hour time period has been a challenging and rewarding journey, as we had to undertake a variety of tasks, such as developing an algorithm to detect items in images, training a machine learning model on a large dataset, and optimizing the model for accuracy. We also had to learn about different syntaxes and techniques for such image classification. Additionally, we had to develop an interface to allow users to receive predictions from the model in real-time using a live webcam. This has been a monumental accomplishment, and we are proud to have achieved such a feat. We are very grateful that we have this opportunity to broaden our horizons and learn so much more about the aforementioned topics.

## What's next for RecycleSorter

We also plan to add more features to our web application and Discord bot, like automatic searching of recycling centers nearby. However, to further expand this project, we will probably need to build a prototype or machine that will be able to identify the type of waste being disposed of and then sort the items into appropriate receptacles. This machine will use cameras to detect the item being disposed of and then make use of artificial intelligence algorithms to classify them into the appropriate categories. This will be combined with hardware components such as motors and conveyor belts to sort the items into the correct receptacles physically. Once this project is expanded, we truly believe that it can make an impact on the recycled waste management industry and keep our environment safe and clean.
