# AirBnB_clone
AirBnB_clone is a simple clone of AirBnB console.
It has implemented abitity to create, update, view
and destroy objects.

## How to install
``git clone https://github.com/musaaj/AirBnB_clone``

## Usage 
``
./console
`` 

## Available Commands 
- create 
**syntax**: ``create ClassName`` 
**available ClassNames**: BaseModel|User|State|City|Place|Amenity|Review 
**Examples**: 
``bash 
create BaseModel 
create Review 
`` 
- show
**syntax**: ``show ClassName instance_id``
**available ClassNames**: BaseModel|User|State|City|Place|Amenity|Review
**Examples**:
``bash
show State i348u-89ued-388489-09903iu
``
- destroy
**syntax**: ``destroy ClassName instance_id``
**available ClassNames**: BaseModel|User|State|City|Place|Amenity|Review
**Examples**:
``bash
destroy Place 937ue-2839-308943-udj8309
``

- all
**syntax**: ``all [ClassName]``
**Examples**:
``bash
all BaseModel
all
``
- update
**syntax**: ``update ClassName instance_id attribute value``
**Examples**:
``bash
update User 937ue-2839-308943-udj8309 email musaaj@gmail.com
``
