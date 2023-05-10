from TTS.utils.synthesizer import Synthesizer

#print("-----starting..")
#print("....configuring model")

model_path = "./model_file.pth"
config_path = "/checkpoint/config.json"

syn = Synthesizer(
     tts_checkpoint=model_path,
     tts_config_path=config_path
 )

#print("...done")


