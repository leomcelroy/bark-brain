BIT_CHOICE = {
  "mdf": {
    "2": {
      "diameter": 2,
      "type": "down-cut"
    },
    "3": {
      "diameter": 2,
      "type": "down-cut"
    },
    "4": {
      "diameter": 3,
      "type": "down-cut"
    },
    "6": {
      "diameter": 3,
      "type": "up-cut"
    },
    "7": {
      "diameter": 3,
      "type": "up-cut"
    },
    "8": {
      "diameter": 3,
      "type": "up-cut"
    },
    "10": {
      "diameter": 3,
      "type": "up-cut"
    },
    "12": {
      "diameter": 4,
      "type": "up-cut"
    },
    "15": {
      "diameter": 4,
      "type": "up-cut"
    },
    "16": {
      "diameter": 6,
      "type": "up-cut"
    },
    "18": {
      "diameter": 6,
      "type": "up-cut"
    },
    "20": {
      "diameter": 8,
      "type": "up-cut"
    },
    "25": {
      "diameter": 8,
      "type": "up-cut"
    },
    "30": {
      "diameter": 10,
      "type": "up-cut"
    },
    "40": {
      "diameter": 12,
      "type": "up-cut"
    },
  },
  "plywood": {
    "2": {
      "diameter": 2,
      "type": "up-cut"
    },
    "3": {
      "diameter": 2,
      "type": "up-cut"
    },
    "4": {
      "diameter": 3,
      "type": "compression"
    },
    "6": {
      "diameter": 3,
      "type": "compression"
    },
    "8": {
      "diameter": 3,
      "type": "compression"
    },
    "10": {
      "diameter": 3,
      "type": "compression"
    },
    "12": {
      "diameter": 4,
      "type": "compression"
    },
    "15": {
      "diameter": 4,
      "type": "compression"
    },
    "16": {
      "diameter": 6,
      "type": "compression"
    },
    "18": {
      "diameter": 6,
      "type": "compression"
    },
    "20": {
      "diameter": 8,
      "type": "compression"
    },
    "25": {
      "diameter": 8,
      "type": "compression"
    },
    "30": {
      "diameter": 10,
      "type": "compression"
    },
    "40": {
      "diameter": 12,
      "type": "compression"
    },
  },
  "plastic": {
    "2": {
      "diameter": 2,
      "type": "down-cut"
    },
    "3": {
      "diameter": 2,
      "type": "up-cut"
    },
    "4": {
      "diameter": 3,
      "type": "up-cut"
    },
    "6": {
      "diameter": 4,
      "type": "up-cut"
    },
    "8": {
      "diameter": 4,
      "type": "up-cut"
    },
    "10": {
      "diameter": 4,
      "type": "up-cut"
    },
    "12": {
      "diameter": 6,
      "type": "up-cut"
    },
    "15": {
      "diameter": 6,
      "type": "up-cut"
    },
    "16": {
      "diameter": 8,
      "type": "up-cut"
    },
    "18": {
      "diameter": 8,
      "type": "up-cut"
    },
    "20": {
      "diameter": 10,
      "type": "up-cut"
    },
    "25": {
      "diameter": 12,
      "type": "up-cut"
    },
    "30": {
      "diameter": 14,
      "type": "up-cut"
    },
    "40": {
      "diameter": 16,
      "type": "up-cut"
    },
  },
  "aluminum": {
    "2": {
      "diameter": 2,
      "type": "up-cut"
    },
    "3": {
      "diameter": 2,
      "type": "up-cut"
    },
    "4": {
      "diameter": 3,
      "type": "up-cut"
    },
    "6": {
      "diameter": 4,
      "type": "up-cut"
    },
    "8": {
      "diameter": 6,
      "type": "up-cut"
    },
    "10": {
      "diameter": 6,
      "type": "up-cut"
    },
    "12": {
      "diameter": 8,
      "type": "up-cut"
    },
    "15": {
      "diameter": 10,
      "type": "up-cut"
    },
    "16": {
      "diameter": 12,
      "type": "up-cut"
    },
    "18": {
      "diameter": 16,
      "type": "up-cut"
    },
    "20": {
      "diameter": 16,
      "type": "up-cut"
    },
    "25": {
      "diameter": 20,
      "type": "up-cut"
    },
    "30": {
      "diameter": 20,
      "type": "up-cut"
    },
    "40": {
      "diameter": 25,
      "type": "up-cut"
    },
  },
  "steel": {
    "2": {
      "diameter": 3,
      "type": "up-cut"
    },
    "3": {
      "diameter": 4,
      "type": "up-cut"
    },
    "4": {
      "diameter": 4,
      "type": "up-cut"
    },
    "6": {
      "diameter": 6,
      "type": "up-cut"
    },
    "8": {
      "diameter": 8,
      "type": "up-cut"
    },
    "10": {
      "diameter": 10,
      "type": "up-cut"
    },
    "12": {
      "diameter": 12,
      "type": "up-cut"
    },
    "15": {
      "diameter": 16,
      "type": "up-cut"
    },
    "16": {
      "diameter": 16,
      "type": "up-cut"
    },
    "18": {
      "diameter": 20,
      "type": "up-cut"
    },
    "20": {
      "diameter": 20,
      "type": "up-cut"
    },
    "25": {
      "diameter": 25,
      "type": "up-cut"
    },
    "30": {
      "diameter": 30,
      "type": "up-cut"
    },
    "40": {
      "diameter": 40,
      "type": "up-cut"
    },
  }
}


SHOPBOT_STIFFNESS = 1500
PRESETS_6MM = {
  "mdf": {
    "chiploads": 0.25,
    "passdepths": 17,
    "rampAngle": 90,
    "hardness": SHOPBOT_STIFFNESS/3000000 
  },
  "wood": {
    "chiploads": 0.2,
    "passdepths": 16,
    "rampAngle": 90,
    "hardness": SHOPBOT_STIFFNESS/1360000
  },
  "hardwood": {
    "chiploads": 0.133,
    "passdepths": 12,
    "rampAngle": 45,
    "hardness": SHOPBOT_STIFFNESS/347289
  },
  "foam_or_wax": {
    "chiploads": 0.3,
    "passdepths": 19,
    "rampAngle": 90,
    "hardness": SHOPBOT_STIFFNESS/19379999
  },
  "plastic_roughing": {
    "chiploads": 0.15,
    "passdepths": 8, 
    "rampAngle": 18,
    "hardness": SHOPBOT_STIFFNESS/371790
  },
  "plastic_finishing": {
    "chiploads": 0.073,
    "passdepths": 8,
    "rampAngle": 18,
    "hardness": SHOPBOT_STIFFNESS/371790
  },
  "aluminum_roughing": {
    "chiploads": 0.12,
    "passdepths": 1.8,
    "rampAngle": 12,
    "hardness": SHOPBOT_STIFFNESS/20000
  },
  "aluminum_finishing": {
    "chiploads": 0.06,
    "passdepths": 1.8,
    "rampAngle": 12,
    "hardness": SHOPBOT_STIFFNESS/20000

  },
  "steel_roughing": {
    "chiploads": 0.08,
    "passdepths": 0.6,
    "rampAngle": 5,
    "hardness": SHOPBOT_STIFFNESS/2000
  },
  "steel_finishing": {
    "chiploads": 0.04,
    "passdepths": 0.6,
    "rampAngle": 5,
    "hardness": SHOPBOT_STIFFNESS/2000
  }
}

def calculateSettings(
  input, 
  plungRateReductionFactor = 0.6, 
  presets6mm = PRESETS_6MM, 
  presetDiameter = 6,
):
  materialToCut = input["materialToCut"]
  millingBitDiameter = input["millingBitDiameter"]
  numberOfFlutes = input["numberOfFlutes"]
  rpm = input["rpm"]
  stiffness = input["stiffness"]

  feedrate = (presets6mm[materialToCut]["chiploads"] * rpm * numberOfFlutes * millingBitDiameter)/presetDiameter
  plungerate = feedrate * plungRateReductionFactor

  fluteReduction = 1-(numberOfFlutes-1)*.15

  preset = presets6mm[materialToCut]["passdepths"]


  passDepth = (preset/presetDiameter*millingBitDiameter)*fluteReduction
  rampAngle = presets6mm[materialToCut]["rampAngle"]

  return {
    "feedrate": feedrate,
    "plungerate": plungerate,
    "passDepth": passDepth,
    "rampAngle": rampAngle
  }

def close(bitChoice, materialThickness):
  counts = [ int(k) for k in bitChoice.keys() ]
  goal = materialThickness

  found = False
  for count in counts:
    if count >= goal and not found:
      found = True
      materialThickness = count

    if goal > counts[len(counts)-1]:
      materialThickness = count

  return materialThickness

def chooseBit(material, materialThickness):
    if material == "wood": 
      material = "plywood"
    elif material == "hardwood": 
      material = "plywood"
    elif material == "plastic_roughing" or material == "plastic_finishing": 
      material = "plastic"
    elif material == "aluminum_roughing" or material == "aluminum_finishing": 
      material = "aluminum"
    elif material == "steel_roughing" or material == "steel_finishing": 
      material = "steel"
    elif material == "foam_or_wax" or material == "mdf": 
      material = "mdf"

    materialThickness = close(BIT_CHOICE[material], materialThickness)
    return BIT_CHOICE[material][str(materialThickness)]


def r(x):
  return round(x, 2)


def adjust(input):
  material = input["materialToCut"]
  bitDiameter = input["millingBitDiameter"]
  flutes = input["numberOfFlutes"]
  rpm = input["rpm"]
  stiffness = input["stiffness"]

  default = calculateSettings(input)

  materialRemovalRate = default["feedrate"]*default["passDepth"]*bitDiameter
  hardness = PRESETS_6MM[material]["hardness"]

  
  mrr = stiffness/hardness

  fluteReduction = 1-(flutes-1)*.15
  rpmFactor = 18000/rpm
  maxPassDepth = mrr/default["feedrate"]/bitDiameter*flutes*fluteReduction/rpmFactor

  pd = maxPassDepth if default["passDepth"] > maxPassDepth else default["passDepth"]

  return {
    "feedrate": r(default["feedrate"]),
    "plungerate": r(default["plungerate"]),
    "passDepth": r(pd),
    "rampAngle": default["rampAngle"],
    "type": chooseBit(material, bitDiameter)["type"]
  }

testChooseBit = chooseBit("mdf", 5)

testSettings = adjust({
  "materialToCut": "wood",
  "millingBitDiameter": 4,
  "numberOfFlutes": 2,
  "rpm": 18000,
  "stiffness": 3000
})

print(testChooseBit)
print(testSettings)


