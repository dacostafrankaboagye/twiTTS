

var audioTrack = WaveSurfer.create({
    container: ".audio",
    waveColor: "#eee",
    progressColor: "red"

});

audioTrack.load("{{ url_for('static', filename='theAudio.wav') }}");


const playBtn = document.querySelector(".play-btn")
const stopBtn = document.querySelector(".stop-btn")
const muteBtn = document.querySelector(".mute-btn")
const volumeSlider = document.querySelector(".volume-slider")

playBtn.addEventListener("click", ()=>{
    audioTrack.playPause();
})

