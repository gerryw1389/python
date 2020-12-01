### Setup

Add yourself as collaborator to this repo. Then make pushes to production.

### ReadJSON

This is a HTTP triggered python app running in Azure Functions that:

1. You pass a two level json payload and it will put them in variables

   ```json
   {
      "name": "gerry",
      "car": "mustang",
      "birth": {
         "city": "fort worth",
         "state": "Texas"
      }
   }
   ```

   - Response:

   ```
   Hello, gerry.

   You chose mustang.

   Your birth city is fort worth in the state of Texas
   ```

2. You can call any of the three functions `ReadJSON`, `ReadJSON2`, or `ReadJSON3`
  - Inside function apps, find the `App Key` blade in Azure and copy the `_master` key
  - Paste it on the end of each URL: `https://{yourApp}.azurewebsites.net/api/ReadJSON?code={_masterKey}`

3. Each of them can import a `helpers.py` function so you can put functions in their own files :)

4. For logging, I tried to modify the `host.json` so that most things are dropped except output.

5. Added a `shared` folder that all functions within the app can use. See `ReadJSON` for calling first function in `shared/shared.py` and `ReadJSON2` for calling second function in `shared/shared.py`

6. Added a way for it to return a json response instead of text (see `ReadJSON`).

  ```json
  [{"response": "Hello, gerry.\n\nYou chose mustang.\n\nYour birth city is fort worth in the state of Texas", "date_time": "2020-11-30-22-48-21"}]
  ```
