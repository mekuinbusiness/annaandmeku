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
const scrollAmount = galleryWrapper ? galleryWrapper.querySelector('.gallery-card')?.offsetWidth + 12 || 300 : 300;
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
    const nameValue = event.target.querySelector('input[data-i18n-ph="ph-name"]').value;
    const attendanceValue = event.target.querySelector('input[name="attendance"]:checked').value;
    const messageValue = event.target.querySelector('textarea').value;

    // Package the data neatly into a JSON object
    const formData = {
        name: nameValue,
        attendance: attendanceValue,
        message: messageValue
    };

    // PASTE YOUR GOOGLE APPS SCRIPT WEB APP URL HERE
    const googleAppScriptUrl = "https://script.google.com/macros/s/AKfycbzb6CXW6Emu7gDft9NuiKJ01wEHWUuA_dAlQ9q9Hpz9Ptd86wDZ5BPuzjJGiLX12USxRQ/exec";

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
        'hero-verse': '“Two are better than one, because they have a good return for their labor. A cord of three strands is not quickly broken.”',
        'hero-reference': '— Ecclesiastes 4:9–12',        'hero-intro': 'You are joyfully invited to celebrate our wedding',        'label-date': 'Date', 'label-day': 'Day', 'label-time': 'Time',
        'save-the-date': 'Save the Date',
        'church-location': 'Ebenezer Evangelical Church \u00b7 Trondheim, Norway',
        'countdown-title': 'The event starts in:',
        'timer-days': 'Days', 'timer-hours': 'Hours', 'timer-mins': 'Mins', 'timer-secs': 'Secs',
        'day-program': 'Day Program',
        'ceremony': '⛪ Wedding Ceremony', 'church-desc': 'Ebenezer Evangelical Church', 'reception': '🏛️ Reception',
        'venue-map': 'Location',
        'rsvp-title': 'RSVP', 'rsvp-deadline': 'Please confirm before July 21, 2026',
        'form-name': 'Your Name', 'form-attend': 'Will you attend?',
        'attend-yes': 'Yes, I will!', 'attend-no': 'Unfortunately, I cannot', 'attend-later': 'I will tell you a bit later',
        'form-message': 'Message to the bride & groom',
        'submit-btn': 'SUBMIT',
        'ph-name': 'Enter your full name', 'ph-message': 'Write your message here…',
        'gift-eyebrow': 'Wedding Gift', 'gift-heading': 'Your Gift',
        'gift-link-label': 'View gift options',
        'gift-message': '<p><strong>Your presence at our wedding is the greatest gift we could receive.</strong></p><p>Should you wish to give a gift, a contribution toward our honeymoon would be sincerely appreciated.</p><p>Thank you for your love, kindness, and for celebrating with us.</p><p><strong>With our heartfelt thanks.</strong></p>',
        'bank-transfer': 'Bank Transfer', 'see-below': '\u2193 see below',
        'iban-label': 'IBAN', 'account-holder': 'Account Holder', 'copy-iban': 'Copy IBAN'
    },
    am: {
        'hero-verse': '«ሁለት ከአንድ ይሻላሉ፤ ምክንያቱም ድካማቸው መልካም ዋጋ አለው። የሶስት ክር ገመድ ቶሎ አይበጠስም።»',
        'hero-reference': '— መጽሐፈ መክብብ 4:9–12',        
        'hero-intro': 'የደስታችን ተካፋይ እንዲሆኑ በደስታ ጠርተነዎታል',        
        'label-date': 'ቀን', 'label-day': 'ዕለት', 'label-time': 'ሰዓት',
        'save-the-date': 'Save the date',
        'church-location': 'ኤቤነዘር ወንጌላዊ ቤተ ክርስቲያን \u00b7 ትሮንድሃይም፣ ኖርዌይ',
        'countdown-title': 'ለሰርጉ ቀን የቀረው ጊዜ:',
        'timer-days': 'ቀናት', 'timer-hours': 'ሰዓታት', 'timer-mins': 'ደቂቃዎች', 'timer-secs': 'ሴኮንዶች',
        'day-program': 'የቀኑ መርሃ ግብር',
        'ceremony': '⛪ የቃልኪዳን ሥነ ሥርዓት', 'church-desc': 'ኤቤነዘር ወንጌላዊ ቤተ ክርስቲያን', 'reception': '🏛️ ራት',
        'venue-map': 'የሠርግ ሥነ ሥርዓት አዳራሽ ቦታ',
        'rsvp-title': 'መገኘቶትን ያሳውቁ', 'rsvp-deadline': 'እባክዎ ከJuly 21፣ 2026 በፊት ያሳውቁን',
        'form-name': 'ስምዎ', 'form-attend': 'ይሳተፋሉ?',
        'attend-yes': 'አዎ፣ እገኛለሁ!', 'attend-no': 'አዝናለሁ፣ መምጣት አልችልም', 'attend-later': 'ትንሽ ቆይቶ እነግርዎታለሁ',
        'form-message': 'ለሙሽሪት እና ሙሽራው መልእክት',
        'submit-btn': 'Submit',
        'ph-name': 'ስም', 'ph-message': 'ለሙሽሪት እና ሙሽው መልእክት ካሎት እዚህ ይጻፉ…',
        'gift-eyebrow': 'የሠርግ ስጦታ', 'gift-heading': 'ስጦታ መስጫዎች',
        'gift-link-label': 'ስጦታ ለሙሽሮች',
        'gift-message': '<p><strong>ትልቁ ስጦታችን በደስታችን መገኘቶ ነው።</strong></p><p>ስጦታ መስጠት ካሰቡ እታች ያሉትን መንገዶች ይጠቀሙ ፡፡ ።</p><p><strong>ከልብ እናመስግናን</strong></p>   ',
        'bank-transfer': 'ለባንክ', 'see-below': '\u2193 ከታች ይመልከቱ',
        'iban-label': 'IBAN', 'account-holder': 'የባለቤቱ ስም', 'copy-iban': 'IBAN '
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

// 6. COPY IBAN TO CLIPBOARD
function copyIban() {
    const iban = document.getElementById('ibanValue').innerText;
    const btn = document.getElementById('copyIbanBtn');
    const label = btn.querySelector('span');
    const originalText = label.innerText;

    navigator.clipboard.writeText(iban).then(() => {
        label.innerText = '\u2713 Copied!';
        btn.style.background = 'var(--primary-burgundy-hover)';
        setTimeout(() => {
            label.innerText = originalText;
            btn.style.background = '';
        }, 2200);
    }).catch(() => {
        // Fallback for older browsers
        const el = document.createElement('textarea');
        el.value = iban;
        el.setAttribute('readonly', '');
        el.style.position = 'absolute';
        el.style.left = '-9999px';
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
        label.innerText = '\u2713 Copied!';
        setTimeout(() => { label.innerText = originalText; }, 2200);
    });
}

