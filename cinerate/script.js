
// Movie Data
const movies = [
    {
        id: 1,
        name: "Inception",
        category: "Action",
        rating: 4.8,
        votes: 10,
        image: "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=400"
    },
    {
        id: 2,
        name: "The Mask",
        category: "Comedy",
        rating: 4.5,
        votes: 8,
        image: "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=400"
    },
    {
        id: 3,
        name: "The Conjuring",
        category: "Horror",
        rating: 4.7,
        votes: 12,
        image: "https://images.unsplash.com/photo-1509248961158-e54f6934749c?w=400"
    },
    {
        id: 4,
        name: "Titanic",
        category: "Romance",
        rating: 4.9,
        votes: 20,
        image: "https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=400"
    },
    {
        id: 5,
        name: "Joker",
        category: "Thriller",
        rating: 4.6,
        votes: 15,
        image: "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=400"
    },
    {
        id: 6,
        name: "Mad Max",
        category: "Action",
        rating: 4.4,
        votes: 9,
        image: "https://images.unsplash.com/photo-1519608487953-e999c86e7455?w=400"
    }
];

// Get HTML elements
const movieContainer = document.getElementById("movieContainer");
const searchInput = document.getElementById("searchInput");
const categoryButtons = document.querySelectorAll(".category-btn");
const languageSelect = document.getElementById("languageSelect");
const API_KEY = "115f5d8e3f18e2fc75ff47a085340fce";
const translations = {
    ta: {
        pageTitle: "திரைப்பட மதிப்பீட்டு இணையதளம்",
        language: "மொழி",
        home: "முகப்பு",
        categories: "வகைகள்",
        movies: "திரைப்படங்கள்",
        heroTitle: "உங்களுக்குப் பிடித்த திரைப்படங்களைக் கண்டறியுங்கள்",
        heroText: "திரைப்படங்கள், வகைகள் மற்றும் மதிப்பீடுகளைப் பாருங்கள்.",
        categoriesTitle: "திரைப்பட வகைகள்",
        popularMovies: "பிரபலமான திரைப்படங்கள்",
        searchPlaceholder: "உங்களுக்குப் பிடித்த திரைப்படத்தைத் தேடுங்கள்...",
        categoryLabel: "வகை",
        ratings: "மதிப்பீடுகள்",
        rateMovie: "மதிப்பிடுங்கள்",
        noMoviesFound: "திரைப்படங்கள் எதுவும் கிடைக்கவில்லை!",
        ratingPrompt: "1 முதல் 5 வரை மதிப்பீடு அளிக்கவும்:",
        invalidRating: "1 முதல் 5 வரை எண்ணை உள்ளிடவும்.",
        thankYou: "மதிப்பிட்டதற்கு நன்றி:",
        categoryNames: {
            All: "அனைத்தும்",
            Action: "அதிரடி",
            Comedy: "நகைச்சுவை",
            Horror: "திகில்",
            Romance: "காதல்",
            Thriller: "திரில்லர்"
        }
    },
    kn: {
        pageTitle: "ಚಲನಚಿತ್ರ ರೇಟಿಂಗ್ ವೆಬ್‌ಸೈಟ್",
        language: "ಭಾಷೆ",
        home: "ಮುಖಪುಟ",
        categories: "ವರ್ಗಗಳು",
        movies: "ಚಲನಚಿತ್ರಗಳು",
        heroTitle: "ನಿಮ್ಮ ನೆಚ್ಚಿನ ಚಲನಚಿತ್ರಗಳನ್ನು ಕಂಡುಕೊಳ್ಳಿ",
        heroText: "ಚಲನಚಿತ್ರಗಳು, ವರ್ಗಗಳು ಮತ್ತು ರೇಟಿಂಗ್‌ಗಳನ್ನು ಅನ್ವೇಷಿಸಿ.",
        categoriesTitle: "ಚಲನಚಿತ್ರ ವರ್ಗಗಳು",
        popularMovies: "ಜನಪ್ರಿಯ ಚಲನಚಿತ್ರಗಳು",
        searchPlaceholder: "ನಿಮ್ಮ ನೆಚ್ಚಿನ ಚಲನಚಿತ್ರವನ್ನು ಹುಡುಕಿ...",
        categoryLabel: "ವರ್ಗ",
        ratings: "ರೇಟಿಂಗ್‌ಗಳು",
        rateMovie: "ರೇಟ್ ಮಾಡಿ",
        noMoviesFound: "ಯಾವುದೇ ಚಲನಚಿತ್ರಗಳು ಕಂಡುಬಂದಿಲ್ಲ!",
        ratingPrompt: "1 ರಿಂದ 5 ರವರೆಗೆ ರೇಟಿಂಗ್ ನೀಡಿ:",
        invalidRating: "1 ರಿಂದ 5 ರವರೆಗಿನ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ.",
        thankYou: "ರೇಟಿಂಗ್ ನೀಡಿದ್ದಕ್ಕಾಗಿ ಧನ್ಯವಾದಗಳು:",
        categoryNames: {
            All: "ಎಲ್ಲಾ",
            Action: "ಸಾಹಸ",
            Comedy: "ಹಾಸ್ಯ",
            Horror: "ಭಯಾನಕ",
            Romance: "ಪ್ರಣಯ",
            Thriller: "ಥ್ರಿಲ್ಲರ್"
        }
    },
    en: {
        pageTitle: "Movie Rating Website",
        language: "Language",
        home: "Home",
        categories: "Categories",
        movies: "Movies",
        heroTitle: "Discover Your Favourite Movies",
        heroText: "Explore movies, categories and ratings.",
        categoriesTitle: "Movie Categories",
        popularMovies: "Popular Movies",
        searchPlaceholder: "Search your favourite movie...",
        categoryLabel: "Category",
        ratings: "ratings",
        rateMovie: "Rate Movie",
        noMoviesFound: "No movies found!",
        ratingPrompt: "Give your rating from 1 to 5:",
        invalidRating: "Please enter a number between 1 and 5.",
        thankYou: "Thank you for rating",
        categoryNames: {
            All: "All",
            Action: "Action",
            Comedy: "Comedy",
            Horror: "Horror",
            Romance: "Romance",
            Thriller: "Thriller"
        }
    },
    hi: {
        pageTitle: "फ़िल्म रेटिंग वेबसाइट",
        language: "भाषा",
        home: "होम",
        categories: "श्रेणियाँ",
        movies: "फ़िल्में",
        heroTitle: "अपनी पसंदीदा फ़िल्में खोजें",
        heroText: "फ़िल्में, श्रेणियाँ और रेटिंग देखें।",
        categoriesTitle: "फ़िल्म श्रेणियाँ",
        popularMovies: "लोकप्रिय फ़िल्में",
        searchPlaceholder: "अपनी पसंदीदा फ़िल्म खोजें...",
        categoryLabel: "श्रेणी",
        ratings: "रेटिंग",
        rateMovie: "रेट करें",
        noMoviesFound: "कोई फ़िल्म नहीं मिली!",
        ratingPrompt: "1 से 5 तक अपनी रेटिंग दें:",
        invalidRating: "कृपया 1 से 5 के बीच की संख्या दर्ज करें।",
        thankYou: "रेटिंग देने के लिए धन्यवाद:",
        categoryNames: {
            All: "सभी",
            Action: "एक्शन",
            Comedy: "कॉमेडी",
            Horror: "हॉरर",
            Romance: "रोमांस",
            Thriller: "थ्रिलर"
        }
    }
};

let selectedCategory = "All";
let currentLanguage = languageSelect.value;

function applyLanguage() {
    const text = translations[currentLanguage];

    document.documentElement.lang = currentLanguage;
    document.title = text.pageTitle;

    document.querySelectorAll("[data-i18n]").forEach(element => {
        element.textContent = text[element.dataset.i18n];
    });

    searchInput.placeholder = text.searchPlaceholder;

    categoryButtons.forEach(button => {
        button.textContent = text.categoryNames[button.dataset.category];
    });

    filterMovies();
}

// Display Movies
function displayMovies(movieList) {

    movieContainer.innerHTML = "";
    const text = translations[currentLanguage];

    if (movieList.length === 0) {
        movieContainer.textContent = text.noMoviesFound;
        return;
    }

    movieList.forEach(movie => {

        const card = document.createElement("div");
        card.className = "movie-card";

        card.innerHTML = `
            <img src="${movie.image}" alt="${movie.name}">

            <div class="movie-info">
                <h3>${movie.name}</h3>

                <p>${text.categoryLabel}: ${text.categoryNames[movie.category]}</p>

                <div class="rating">
                    ⭐ ${movie.rating.toFixed(1)} / 5
                    <small>(${movie.votes} ${text.ratings})</small>
                </div>

                <button class="rate-btn" data-id="${movie.id}">
                    ${text.rateMovie}
                </button>
            </div>
        `;

        movieContainer.appendChild(card);
    });
}

// Filter Movies
function filterMovies() {

    const searchText = searchInput.value.toLowerCase();

    const filteredMovies = movies.filter(movie => {

        const matchesCategory =
            selectedCategory === "All" ||
            movie.category === selectedCategory;

        const matchesSearch =
            movie.name.toLowerCase().includes(searchText);

        return matchesCategory && matchesSearch;
    });

    displayMovies(filteredMovies);
}

// Category Button Click
categoryButtons.forEach(button => {

    button.addEventListener("click", () => {

        categoryButtons.forEach(btn =>
            btn.classList.remove("active")
        );

        button.classList.add("active");

        selectedCategory = button.dataset.category;

        filterMovies();
    });
});

// Search Movies
searchInput.addEventListener("input", filterMovies);

// Rate Movie
movieContainer.addEventListener("click", event => {

    if (event.target.classList.contains("rate-btn")) {

        const movieId = Number(event.target.dataset.id);

        const movie = movies.find(m => m.id === movieId);

        const userRating = Number(
            prompt(translations[currentLanguage].ratingPrompt)
        );

        if (!Number.isFinite(userRating) ||
            userRating < 1 ||
            userRating > 5) {

            alert(translations[currentLanguage].invalidRating);
            return;
        }

        // Calculate new average rating
        movie.rating =
            ((movie.rating * movie.votes) + userRating) /
            (movie.votes + 1);

        movie.votes++;

        alert(translations[currentLanguage].thankYou + " " + movie.name + "!");

        filterMovies();
    }
});

languageSelect.addEventListener("change", () => {
    currentLanguage = languageSelect.value;
    applyLanguage();
});

// Initial Display
document.querySelector('[data-category="All"]').classList.add("active");
applyLanguage();

