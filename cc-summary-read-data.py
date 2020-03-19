import os
import json

# get list of file from cc-summary
fileList = os.listdir("cc-summary")

for fileName in fileList:
  # Read data from file
  print("Open data from file ...")
  cc_summary_file = open("cc-summary/" + fileName, "r")

  # Change to JSON
  print("Read data ...")
  cc_summary_json = json.loads(cc_summary_file.read())

  # Prepare UI Test JSON
  ui_test_json = {}
  index = 1

  # List Card from cc summary API
  print("Save data ...")
  card_list = cc_summary_json["cardList"]
  for card in card_list:

    # Save data from json
    ui_test_json["creditCard%d" % index] = {
      "cardName": card["productType"]["description"],
      "cardMaskFormat": card["cardRefNo"]
    }
    index = index + 1

  # Write data to file
  print("Write data to UI test file ...")
  ui_file = open("cc-summary-ui/" + fileName[:-5] + "_ui.json", "w+")
  ui_file.write(json.dumps(ui_test_json))

  # Close file
  print("Close file ...")
  cc_summary_file.close()
  ui_file.close()

  print("Complete!")