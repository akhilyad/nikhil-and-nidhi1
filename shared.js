/* Shared by the groom and bride links. Edit here once; both pages read it.
   Wording below is not yet checked by a native reader. Please have a family elder read it before the cards go out. */

/* After this moment the site turns itself into a thank-you page (India time). Add ?thanks=1 to any link to preview it. */
const THANKS = {
  from: "2026-12-16T00:00:00+05:30",
  albumUrl: "",    /* view-only folder with the photographer's photos; the button shows only when this is filled in */
  uploadUrl: ""    /* shared Google Photos album where guests add their own photos; the button shows only when filled in */
};

/* Second lines under the English text. Groom link: Hindi. Bride link: Kannada.
   ev: keyed by the exact English event title used in DAYS on the page. */
const L2 = {
  groom: {
    lang: 'hi',
    cover: 'शुभ विवाह',
    invite: 'सादर आमंत्रण',
    flow: 'तीन दिन का उत्सव',
    venue: 'स्थान',
    rsvp: 'कृपया उत्तर दें',
    thanks: 'धन्यवाद',
    ev: {
      'Haldi Ceremony': 'हल्दी',
      'Var Pooja, Tilak & Engagement': 'वर पूजा, तिलक एवं सगाई',
      'Baraat': 'बारात',
      'Sangeet': 'संगीत',
      'Dinner': 'भोज',
      'Muhurtham': 'मुहूर्त',
      'Reception & Lunch': 'प्रीति भोज एवं भोजन',
      'Reception': 'प्रीति भोज'
    },
    blessing: '॥ श्री गणेशाय नमः ॥',
    mantra: ['वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ ।', 'निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा ॥']
  },
  bride: {
    lang: 'kn',
    cover: 'ಶುಭ ವಿವಾಹ',
    invite: 'ಆದರದ ಆಹ್ವಾನ',
    flow: 'ಮೂರು ದಿನಗಳ ಸಂಭ್ರಮ',
    venue: 'ಸ್ಥಳ',
    rsvp: 'ದಯವಿಟ್ಟು ಉತ್ತರಿಸಿ',
    thanks: 'ಧನ್ಯವಾದಗಳು',
    ev: {
      'Haldi Ceremony': 'ಅರಿಶಿನ',
      'Var Pooja, Tilak & Engagement': 'ವರಪೂಜೆ, ತಿಲಕ ಮತ್ತು ನಿಶ್ಚಿತಾರ್ಥ',
      'Baraat': 'ಬರಾತ್',
      'Sangeet': 'ಸಂಗೀತ',
      'Dinner': 'ಭೋಜನ',
      'Muhurtham': 'ಮುಹೂರ್ತ',
      'Reception & Lunch': 'ಆರತಕ್ಷತೆ ಮತ್ತು ಭೋಜನ',
      'Reception': 'ಆರತಕ್ಷತೆ'
    },
    blessing: '॥ ಶ್ರೀ ಗಣೇಶಾಯ ನಮಃ ॥',
    mantra: ['ವಕ್ರತುಂಡ ಮಹಾಕಾಯ ಸೂರ್ಯಕೋಟಿ ಸಮಪ್ರಭ ।', 'ನಿರ್ವಿಘ್ನಂ ಕುರು ಮೇ ದೇವ ಸರ್ವಕಾರ್ಯೇಷು ಸರ್ವದಾ ॥']
  }
};
