# Piza and Steak Images Predictions
## Installation
To install this project, follow these steps in windows

1. Clone the repository :
```bash
git clone https://github.com/gurwindaniel/pizza_steak_ai.git
```
## Usage Instructions
2. Create an Python environmental Variable :
  ```bash
pip install venv
```
``` bash
python -m venv my_env
```
3. Activate Environmental Variable :
   ```bash
   .\my_env\Scripts\activate
   ```
4. Install Requirements :
```bash
pip install -r requirments.txt
```
5. Start the Application : In terminal run
```bash
streamlit run app.py
```
6. Upload the steak or pizza image for predictions

Pizza_steak.h5 is the custom model.
Pizza_steak_fine.h5 is the fine tuned model from MobileNetV2 (transfer learning)
