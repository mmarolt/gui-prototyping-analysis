import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

generated_guis_path = '../generated_guis'
prompt_names = ['instruction', 'pd_zs', 'pd_fs', 'ref_instruction']

app_ids = [name for name in os.listdir(generated_guis_path) if os.path.isdir(os.path.join(generated_guis_path, name))]

prototype_files = []
for app_id in app_ids:
    for prompt in prompt_names:
        html_path = os.path.join(generated_guis_path, str(app_id), f'{prompt}.html')
        if os.path.isfile(html_path):
            prototype_files.append({'app_id': app_id, 'method': prompt, 'path': html_path})

chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless (no UI)
chrome_options.add_argument('--allow-file-access-from-files')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--log-level=3')
chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

results = []
driver = webdriver.Chrome(options=chrome_options)

for proto in prototype_files:
    file_url = 'file://' + os.path.abspath(proto['path'])
    driver.get(file_url)

    driver.implicitly_wait(2)

    logs = driver.get_log('browser')
    error_messages = [log['message'] for log in logs if log['level'] == 'SEVERE']
    results.append({
        'app_id': proto['app_id'],
        'prompt': proto['prompt'],
        'errors': len(error_messages),
        'error_descriptions': ' || '.join(error_messages)
    })

driver.quit()

df = pd.DataFrame(results)
df.to_csv('console_errors.csv', index=False, sep=';')