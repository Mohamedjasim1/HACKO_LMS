// // Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";
// // TODO: Add SDKs for Firebase products that you want to use
// // https://firebase.google.com/docs/web/setup#available-libraries

// // Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBB8gdMlNhV7ULycr1RscXsi1M9vXFimlE",
  authDomain: "codespot-1e27c.firebaseapp.com",
  projectId: "codespot-1e27c",
  storageBucket: "codespot-1e27c.appspot.com",
  messagingSenderId: "799590572256",
  appId: "1:799590572256:web:67a3148d4cbfb79a423085"
};

// // Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
auth.languageCode = 'en';
const provider = new GoogleAuthProvider();

const googleLogin = document.getElementById('google-login-btn');
googleLogin.addEventListener('click', function(){
    
    console.log("hi");
    signInWithPopup(auth, provider).then((result) => {
    console.log("nalla iruka");
    const credential = GoogleAuthProvider.credentialFromResult(result);
    const token = credential.accessToken;
    const user = result.user;
    console.log(user);
    window.location.href = 'http://127.0.0.1:8000/studentDashboard/course'; //TODO: CHANGE THIS TO DOMAIN NAME

  }).catch((error) => {
    console.log("periya error");
    const errorCode = error.code;
    const errorMessage = error.message;
    const email = error.customData.email;
    const credential = GoogleAuthProvider.credentialFromError(error);
    console.log(error);
  });
})


// import { signInWithRedirect } from "firebase/auth";
// import { getRedirectResult } from "firebase/auth";

// const auth = getAuth();

// const googleLogin = document.getElementById('google-login-btn');
// googleLogin.addEventListener('click', function(){
// console.log("bye");
// getRedirectResult(auth).then((result) => {

//      console.log("romba nalla iruka1");
//     // This gives you a Google Access Token. You can use it to access Google APIs.
//     const credential = GoogleAuthProvider.credentialFromResult(result);
//     console.log("romba nalla iruka2");
//     const token = credential.accessToken;

//     console.log("romba nalla iruka3");
//     // The signed-in user info.
//     const user = result.user;
//     console.log("romba nalla iruka4");
//     // IdP data available using getAdditionalUserInfo(result)
//     // ...
//   }).catch((error) => {
//     // Handle Errors here.
//     console.log("romba periya error");
//     const errorCode = error.code;
//     const errorMessage = error.message;
//     // The email of the user's account used.
//     const email = error.customData.email;
//     // The AuthCredential type that was used.
//     const credential = GoogleAuthProvider.credentialFromError(error);
//     console.log(error);
//     // ...
//   });
// })
