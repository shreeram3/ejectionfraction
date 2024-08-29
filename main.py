from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import sys


# for getting programes from utilities folders
sys.path.insert(0, './utilities')

from videotoframe import convert_video_to_frames
from imageprocess import apply_bilateral_filter
# from segmentation import process_images
app = FastAPI()
app.mount("/static", StaticFiles(directory="chambers"), name="static")
app.mount("/static", StaticFiles(directory="Uploads"), name="static")

PATH_FRAMES_2CH ="C:\\Project_1\\FastApi2\\chambers\\2ch\\frames"
PATH_FILTERED_FRAMES_2CH = "chambers/2ch/filter_frame" 
PATH_PROCESS_FRAMES_2CH = "chambers/2ch/processed_frames"
NUM_FRAMES = 150
# saving file to local host
@app.post("/upload/")
async def uploadfile(files: list[UploadFile]):
    try: 
        for file in files:
            file_path = f"C:\\Project_1\\FastApi2\\Uploads\\{file.filename}"
            with open(file_path, "wb") as f:
                f.write(file.file.read())
                print({"message": "File saved successfully"})
            # convert_video_to_frames(file_path, PATH_FRAMES_2CH, NUM_FRAMES )
            # apply_bilateral_filter(PATH_FRAMES_2CH,PATH_FILTERED_FRAMES_2CH )
            # process_images(PATH_FILTERED_FRAMES_2CH,PATH_PROCESS_FRAMES_2CH)


        content = f"""
<html>
<body>
<img src = "http://127.0.0.1:8000/static/2ch/filter_frame/frame_0000.jpg"/>
<img src = "http://127.0.0.1:8000/static/2ch/filter_frame/frame_0000.jpg"/>
<video autoplay > 
<source src = "http://127.0.0.1:8000/static/cha1.mp4" type="video/mp4">
</source>
</video>
</body>
<html>
"""
        
        content1 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejection Fraction</title>
    <link rel="stylesheet" href="static/style.css">
</head>
<body>
    <div>
        <center>

            <h1>Ejection Fraction</h1>
        </center>
    </div>
    <div class="wrapper">
        <div class="left_div">
            <!-- image of 2ch and 4ch [both endsystole and disystole] -->
        <div class="left_div_images">
            <div>
            <img src = "http://127.0.0.1:8000/static/2ch/filter_frame/frame_0000.jpg"/>
            </div>
            <div>
            <img src = "http://127.0.0.1:8000/static/2ch/filter_frame/frame_0000.jpg"/>
            </div>
            <div>
             <img src = "http://127.0.0.1:8000/static/2ch/filter_frame/frame_0000.jpg"/>
            </div>
            <div>
             <img src = "http://127.0.0.1:8000/static/2ch/filter_frame/frame_0000.jpg"/>
            </div>
        </div>

             <!-- bottom div to show ejection fraction -->
        <div class="left_div_ejection_fraction">
            Ejection Fraction : 0.8
        </div> 
        </div>
        <!-- video of heart -->
        <div class="right_div">
            <div class="video_div">
                <video autoplay muted controls > 
<source src = "http://127.0.0.1:8000/static/cha2.mp4" type="video/mp4">
</source>
</video>
            </div>
            <div class="video_buttons">
                <button>Normal</button>
                <button>Masked</button>
            </div>
        </div>
    </div>
   <style>
   body{
   background: black;
   color : white;
    padding: 0;
    margin: 0;
}
.wrapper{
    max-width: 100vw;
    height: 90vh;
    background-color: black;
    display: grid;
    grid-template-columns: 0.5fr 1fr;
}

img{
width : 100%;
height : 100%
}
.left_div{


}
.left_div_images{
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;}

.left_div_images div {
    height:211px ;
    width: 318px;
  
    margin: 1rem;
}
.left_div_ejection_fraction{
    margin : 20px auto;
    background-color: aquamarine;
    border-radius : 10px;
    height: 56px;
    width: 60%;
    display :flex;
    align-items : center;
    justify-content : center;
    color : black;
    font-size : 24px;
}
.right_div .video_div{
    margin: 1rem;
    width: 95%;
    height: 80%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.video_buttons{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.video_buttons button{
    margin: 1rem;
    padding: 0.5rem 1rem;
    border: none;
}
   </style>
    
</body>
</html>

"""
        return HTMLResponse(content=content1)
        
    except Exception as e:
        return {"message": e.args}
    
@app.get("/")
def root():
    content = """
<!DOCTYPE html>
<html>
<head>
    <title>GFG</title>
</head>
<body>
    <h2>Geeks for Geeks </h2>
    <form action="http://127.0.0.1:8000/upload" method="POST" enctype="multipart/form-data">
        <!-- File input field -->
        <label for="file">Choosen file will be saved on server :</label>
        <input type="file" name="files" accept=".jpg" multiple>
     
        <br><br>
         
        <!-- Submit button -->
        <input type="submit" value="Upload">
    </form>
</body>
</html>
"""
    return HTMLResponse(content=content)