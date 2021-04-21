from .coco import CocoDataset

class SDCDataset(CocoDataset):

    CLASSES = ('ship', )

class SDCDataset_MultiDet(CocoDataset):

    CLASSES = ('Cargo vessel','Ship','Motorboat','Fishing boat','Destroyer','Tugboat','Loose pulley','Warship','Engineering ship','Amphibious ship','Cruiser','Frigate','Submarine','Aircraft carrier','Hovercraft','Command ship')