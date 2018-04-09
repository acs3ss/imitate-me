# imitate-me

![Reflxetion logo dancing](/imgs/logo-alex.jpg)
![Reflextion logo soccer](/imgs/logo-abhishek.jpg)

## Inspiration:

Our inspiration was to create a means for people to step into the spotlight with their idols and learn to move as they do. To shake and pound it like a hip-hop master, to strike blows like an elite martial artist, and learn to dribble a basketball like an NBA baller. Reflextion allows someone to see how they match up to the best.
What it does:

Currently, Reflextion has the capabilities of recording a video of someone wearing the Myo™ Gesture Control Armband and mapping the movements of the said person. The mapping data is currently stored locally, and when played back against a person wearing the Myo™ it will calculate how closely they match the movements and intensity of the person in the video.
Why we made it:

These functionalities were thought about for multi-use purposes. We designed a web application that would promote activity, a healthier lifestyle, and also be a fun and interactive way to learn new moves from athletes, artists and anyone from all over the world. We also designed this web application with the intention that a wide variety of activities would be covered such as weight-lifting form, yoga motions, and make the barriers for entry for these types of activities less daunting and more accessible for everyone as well as preventing injuries for a long-lasting active lifestyle.
How we built it:

The initial step for our hack was to first and foremost mess around with the Myo™ band. This involved testing the capabilities and limitations of the product by coming up with test case motions and maneuvers and navigating through various applications to see its use.

After this test period, we figured out the configuration of the Myo™ and were able to extract the data from the device and interpret the results from the gyroscope, accelerometer and other measuring mechanisms. We then collected the data as JSON objects and then spent a good amount of time building the front end of the website application. We made it possible to record and upload videos that were then able to be used as mapping data to compare the user to the original video. Switching over to the backend, we managed to make the API that would receive the Myo™ data and then convert that data into a score of the user's performance to see how they compared to the model.

## Challenges we ran into:

Oh, boy was this a doozy.

After a Friday of little to no productivity and two to three hours of shooting ideas until something hit, we decided to buckle down and start on our project. Sadly, the first idea that we agreed upon doing ended up being a bust as we were unable to differentiate our hack as much as we planned and thus after sinking five hours, we turned our gaze to a new frontier.

Starting fresh in the wee hours of the morning, we began to work on Reflextion, and the hurdles to progress came frequent and fast. The initial issue was integrating a webcam service into our product since we were making a website application. Due to this dilemma, we had to resort to uploading videos instead of taking them directly on the website. Additionally, there was also an issue with storing our data in databases and utilizing MongoDB Stitch into our web application.
Accomplishments that we're proud of:

We are proud that we managed to make an API that can receive the motion mapping data and return feedback as well as a score of the user’s performance.

## What we learned:

We learned how to make an API as well as how to develop a model by utilizing machine learning.
What's next for Reflextion:

The next step for Reflextion is to introduce a means for the data that is currently stored locally to stored in a globally accessible database. This way anyone with a Myo™ would be able to access and learn how anyone from across the world performs in almost all water-free activities. Additionally, we want to incorporate multiple Myo™s so that users would be able to map all motions from the arms and legs to make it an incredibly comprehensive way to mimic motion. As well, we plan on making a mobile application for Reflextion.
