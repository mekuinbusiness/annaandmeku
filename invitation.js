// 1. COUNTDOWN TIMER ENGINE
// Set target date (September 19, 2026 at 11:00:00)
const targetDate = new Date("Sep 19, 2026 11:00:00").getTime();

function updateCountdown() {
    const now = new Date().getTime();
    const difference = targetDate - now;

    if (difference < 0) {
        document.getElementById("days").innerText = "00";
        document.getElementById("hours").innerText = "00";
        document.getElementById("minutes").innerText = "00";
        document.getElementById("seconds").innerText = "00";
        return;
    }

    const d = Math.floor(difference / (1000 * 60 * 60 * 24));
    const h = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const m = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
    const s = Math.floor((difference % (1000 * 60)) / 1000);

    document.getElementById("days").innerText = d < 10 ? "0" + d : d;
    document.getElementById("hours").innerText = h < 10 ? "0" + h : h;
    document.getElementById("minutes").innerText = m < 10 ? "0" + m : m;
    document.getElementById("seconds").innerText = s < 10 ? "0" + s : s;
}
setInterval(updateCountdown, 1000);
updateCountdown();

// 2. ACCORDION TOGGLE INTERACTION
const headers = document.querySelectorAll(".accordion-header");
headers.forEach(header => {
    header.addEventListener("click", function() {
        const item = this.parentElement;
        const content = this.nextElementSibling;

        if (item.classList.contains("active")) {
            content.style.maxHeight = null;
            item.classList.remove("active");
        } else {
            // Close other active sections
            document.querySelectorAll(".accordion-item").forEach(el => {
                el.classList.remove("active");
                el.querySelector(".accordion-content").style.maxHeight = null;
            });

            content.style.maxHeight = content.scrollHeight + "px";
            item.classList.add("active");
        }
    });
});

// 3. SCROLL-DRIVEN REVEAL ANIMATIONS
function revealOnScroll() {
    const reveals = document.querySelectorAll(".reveal");
    const windowHeight = window.innerHeight;

    reveals.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        // Elements trigger animation when they are 100px from entering the view
        if (elementTop < windowHeight - 100) {
            element.classList.add("active");
        }
    });
}
window.addEventListener("scroll", revealOnScroll);
// Initial execution to show elements above the fold on load
window.addEventListener("load", revealOnScroll);

const galleryWrapper = document.getElementById("galleryWrapper");
const scrollAmount = 280;
document.querySelectorAll(".gallery-nav").forEach(button => {
    button.addEventListener("click", () => {
        if (!galleryWrapper) return;
        const direction = button.classList.contains("next") ? 1 : -1;
        galleryWrapper.scrollBy({ left: direction * scrollAmount, behavior: "smooth" });
    });
});

// 4. RSVP FORM SUBMISSION HANDLER
function handleFormSubmit(event) {
    event.preventDefault(); // Stop the page from reloading

    // Grab the Submit button to show a loading state
    const submitBtn = event.target.querySelector('.submit-btn');
    const originalBtnText = submitBtn.innerText;
    submitBtn.innerText = "SENDING...";
    submitBtn.disabled = true;

    // Collect the form input values
    const nameValue = event.target.querySelector('input[placeholder*="name"]').value;
    const attendanceValue = event.target.querySelector('input[name="attendance"]:checked').value;
    const intolerancesValue = event.target.querySelector('input[placeholder*="Vegetarian"]').value;

    // Package the data neatly into a JSON object
    const formData = {
        name: nameValue,
        attendance: attendanceValue,
        intolerances: intolerancesValue
    };

    // PASTE YOUR GOOGLE APPS SCRIPT WEB APP URL HERE
    const googleAppScriptUrl = "https://script.google.com/macros/s/AKfycbxrgV-vQS9-ljRhS9XsUcTmE3OsCGmuKHyJzO9YZwPt7dfz3FhJkr3vv3NJrHCcRIMaYQ/exec";

    // Send the data securely via a POST request
    fetch(googleAppScriptUrl, {
        method: 'POST',
        mode: 'no-cors', // Prevents cross-origin safety errors on static sites
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(() => {
        // Since we are using 'no-cors', we assume a successful post trigger
        alert("Thank you! Your RSVP response has been safely recorded.");
        document.getElementById("weddingRsvpForm").reset();
    })
    .catch(error => {
        console.error('Submission error:', error);
        alert("Oops! There was an issue submitting your RSVP. Please try again.");
    })
    .finally(() => {
        // Reset the button back to normal
        submitBtn.innerText = originalBtnText;
        submitBtn.disabled = false;
    });
}

// 5. LANGUAGE SWITCHER
const i18n = {
    en: {
        'hero-verse': 'Two are better than one',
        'hero-reference': 'a cord of three strands is not quickly broken.<br>Eccl 4:9\u201312',
        'label-date': 'Date', 'label-day': 'Day', 'label-time': 'Time',
        'save-the-date': 'Save the Date',
        'church-location': 'Ebenezer Evangelical Church \u00b7 Trondheim, Norway',
        'countdown-title': 'The event starts in:',
        'timer-days': 'Days', 'timer-hours': 'Hours', 'timer-mins': 'Mins', 'timer-secs': 'Secs',
        'day-program': 'Day Program',
        'ceremony': 'Wedding Ceremony', 'church-desc': 'Ebenezer Evangelical Church', 'reception': 'Reception',
        'venue-map': 'Venue Map',
        'rsvp-title': 'RSVP', 'rsvp-deadline': 'Please confirm before July 21, 2026',
        'form-name': 'Your Name', 'form-attend': 'Will you attend?',
        'attend-yes': 'Yes, I will!', 'attend-no': 'Unfortunately, I cannot', 'attend-later': 'I will tell you a bit later',
        'form-intolerance': 'Do you have any food intolerances?',
        'submit-btn': 'SUBMIT',
        'ph-name': 'Enter your full name', 'ph-intolerance': 'e.g., Vegetarian, Nut Allergy, None'
    },
    am: {
        'hero-verse': 'ሁለት ከአንድ ይሻላሉ',
        'hero-reference': 'የሶስት ክር ገመድ ቶሎ አይበጠስም።<br>መ.ጠ. 4:9\u201312',
        'label-date': 'ቀን', 'label-day': 'ዕለት', 'label-time': 'ሰዓት',
        'save-the-date': 'ቀኑን ያስታውሱ',
        'church-location': 'ኤቤነዘር ወንጌላዊ ቤተ ክርስቲያን \u00b7 ትሮንድሃይም፣ ኖርዌይ',
        'countdown-title': 'ዝግጅቱ የሚጀምርበት ጊዜ:',
        'timer-days': 'ቀናት', 'timer-hours': 'ሰዓታት', 'timer-mins': 'ደቂቃዎች', 'timer-secs': 'ሴኮንዶች',
        'day-program': 'የቀን መርሃ ግብር',
        'ceremony': 'የሠርግ ሥነ ሥርዓት', 'church-desc': 'ኤቤነዘር ወንጌላዊ ቤተ ክርስቲያን', 'reception': 'አቀባበል',
        'venue-map': 'የቦታ ካርታ',
        'rsvp-title': 'ምላሽ', 'rsvp-deadline': 'እባክዎ ከጁላይ 21፣ 2026 በፊት ያረጋግጡ',
        'form-name': 'ስምዎ', 'form-attend': 'ይሳተፋሉ?',
        'attend-yes': 'አዎ፣ እገኛለሁ!', 'attend-no': 'አዝናለሁ፣ መምጣት አልችልም', 'attend-later': 'ትንሽ ቆይቶ እነግርዎታለሁ',
        'form-intolerance': 'የምግብ አለርጂ አለዎት?',
        'submit-btn': 'አስገባ',
        'ph-name': 'ሙሉ ስምዎን ያስገቡ', 'ph-intolerance': 'ለምሳሌ፡ አትክልተኛ፣ ለውዝ አለርጂ፣ የለም'
    }
};

function switchLanguage(lang) {
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (i18n[lang] && i18n[lang][key] !== undefined) el.innerHTML = i18n[lang][key];
    });
    document.querySelectorAll('[data-i18n-ph]').forEach(el => {
        const key = el.getAttribute('data-i18n-ph');
        if (i18n[lang] && i18n[lang][key] !== undefined) el.placeholder = i18n[lang][key];
    });
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === lang);
    });
}

document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => switchLanguage(btn.dataset.lang));
});
