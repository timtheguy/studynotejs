# StudyNoteJS 
##Summary
The StudyNote.JS web application is designed for those with a lot to read, and not enough time to read it. The algorithms in our solution provide an easy way to convert large chunks of boring and long text into quick and easy to read bullet points.

Through careful processing of each word, and the use of machine learning via the DatumBox API, we are able to select just the right balance of content and brevity to deliver a highly portable PDF document right in your web browser. The DatumBox API is accessed through a Python-dependent backend, which is able to be leveraged by Amazon AWS cloud severs. A variety of formatting options are available to make your study experience comfortable for any eyes.

On those long nights of research, an easy-to-use extension to the Google Chrome web browser allows users to condense pieces of articles into slick statements that are easy to discern and categorize with a quick glance. The aforementioned API from DatumBox helps to lift that burden too by assessing the complexity of the processed text and assigning one of 16 topics to the bulleted content.

### Demo
Check out [our client-side demo](http://timtheguy.github.io/studynotejs/) (not completely functional).

### Installing
Clone the repository to your machine and open the _index.html_ file in your web browser of choice (preferrably Google Chrome)

The Python back end is not explicitly interfaced with the front-end index.html. Feel free to clone the Python back-end

### Built With
* [Bootstrap (v3.3.6)](http://getbootstrap.com) - Web framework used
* [jsPDF](https://parall.ax/products/jspdf) - The client-side PDF generation library 
* [DatumBox Machine Learning API](http://www.datumbox.com/machine-learning-api/) - The machine learning API implemented

### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


### Acknowledgments
This project was originally built at the Swamphacks 2016 hackathon held at the University of Florida.
Check out [our hackathon submission on Devpost.](http://devpost.com/software/studynote-js)
