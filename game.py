"""LISTE DE FONCTION

    - qui lit et qui crée la structure de donnée (=file_to_database) 
    - qui affiche le plateau (portail, asteroïde) (=board display) 
    - remplit la liste des minerais de joueur. [4, 4] (=tiny_fucking_fonction)

    NOTE: Soit ATTAQUE SOIT DEPLACEMENT
    
    NOTE: D ABORD DEPLACEMENT PUIS ATTAQUE
    (INPUT)

    BOUCLE  
    - qui interprète les commandes et vérifie la légalité des coups(ignorer).(=order_treatment)
        - Si Achat (Ajoute le vaisseaux dans la structure de donnée) (=buy_order)
        - Si Lock/Release (Change la propriété Lock/Release dans la grille) (=release_or_lock)
        - Si Déplacement (Change les coordonnées du/des vaisseaux concernés dans la structure) (=ships_shifting)
        - Si Attaque (Setup une liste des cases touchées) (=AI_decision_making)



    
    - Prise en compte des effets
        (Test pour savoir s'il y a un/des vaisseaux puis on diminue les pv si touché(s) et
         on le retire si 0 pv)
        (Si portail down fin de partie)
        (Asteroid détruit si plus de minerai)
        (Réaffichage)


NOTE POUR UI : Un centre diffèrent par ship.
           Une couleur par équipe
           Le centre est tjs au dessus"""






def file_to_data_base(file_name):
    """Read the .mw file and  extract a data structure from it.
    Parameters
    ----------
    file_name: name of the  .mw file (string)
    
    Notes
    -----
    Portals are contained in a list of two elements, the portals of players 1 and 2
    are elements 0 and 1 (it will be more practical to say player 0 and 1, not 1 and 2)
    
    Return
    ------
    file_database: dictionnary of data extracted from the .mw file (dict)
    
    """
    mw_file = file.open(file_name,'r')
    file_data = mw_file.readline()
    
        

    
def ships_caracteristics_fonction():
    """Create a data structure containing the informations of ships (types)
    
    Return
    ------
    ships_caracteristics: a dictionnary containing the ships caracteristics (dict)
    """
    
def board_display(file_database,elements):
    """Print the board in its actual settings
    
    Parameters
    ----------
    file_database: data base extracted from the .mv file (dict)
    elements: data base containing every elements present on the board and their informations(dict)
    
    Notes
    -----
    The file_structure data base is used to first print the board, 
    to actualize it after every turn we will use the elements data base.
    """
    
def set_up_money():
    """Create a list that will stock the money of both 'players'
    At frist it's a two elements list: [4,4]
    
    Return:
    ------
    current_money: list stocking the current money of the two 'players' (list)
    """
    
def AI_decision_making():
    """Returns the order of the artificial intelligence for every turn
    
    Returns
    -------
    AI_order: AI's order to execute on this turn (string)
    """
    
def order_parser(order_0,order_1):
    """Parsing orders and execute them if their are confirmed as 'legal'
    
    Parameters
    ----------
    order_0: order encoded by the first player
    order_1: order encoded by the second player
    
    Raise
    -----------
    ValueError: order_0 must be defined
    ValueError: order_1 must be defined
    """
    
    
   
def is_legal_move(order): 
    """Return True is the order 
    Parameters
    ----------
    order: order encoded
    
    Return
    ------
    legality_check (bool
    
    Raise
    -----------
    ValueError: order must be defined
    
    Version
     -------
     specification: Yohan Noël-huls (v.1 03/03/2016)
    """

def buy_order(ship_to_buy):
    """Execute a buy order
    Parameters
    ----------
    ship_to_buy: the ship that the user is buying (string)
    
    Raise
    ---------
    ValueError: ship_to_buy must be a kind of a ship which existed
    """
def release_or_lock_order():
    """Release if the ship is locked and lock if the ship is released. 
    """
     
def ship_shifting(x,y,element):
    """ Update the coordinates of the ship
    Parameters
    ----------
    x : absciss of the updated place of the ship (int)
    y : ordinate of the updated place of the ship (int)
    element: the ship which moves(dict)
    
    Raise
    --------
    ValueError: x is within 0 and width of board
    ValueError: y is within 0 and height of board
    ValueError: ship_shifting must be defined """
    
def attack_order(x_attack, y_attack, targeted_cases): 
    """Take the attack's coordinates returns every case's coordinates of the board where an attack has been ordered
    
    Parameters
    ----------
    x: absciss of the attack's coordinates (int)
    y: ordinate of the attack's coordinates (int)
    
    Returns
    -------
    targeted_cases: list of list ([[x1,y1],[x2,y2],...]) of all the cases that will be attacked on this turn (list)
    
    Raise
    --------
    ValueError: x_attack must be defined
    ValueError: y_attack must be defined  
    ValueError: targeted_case must be defined
    
         
     Version
     -------
     specification: Yohan Noël-huls (v.1 03/03/2016)
   
    """
    
def damage_applier(targeted_cases, database):
    """Apply attacks order once the ships have been moved to the case aimed on this turn

    Parameters    
    ----------
    targeted_cases: list of list ([[x1,y1],[x2,y2],...]) of all the cases that will be attacked on this turn (list)
    database: data base containing every elements present on the board and their informations(dict)
    
     Raise
     --------
     ValueError: targeted_cases must existed
     ValueError: database must existed
     
          
     Version
     -------
     specification: Yohan Noël-huls (v.1 03/03/2016)

    """

def element_destroy(elements, name): 
    """Destroy an element, who get hit, if his life/ores reaches 0 or lower

    Parameters
    ----------
    elements: database of all the elements on the board (dict) 
    name: name of the element (string)
    
    Return
    ------   
    elements: database of all the elements on the board (dict)
     
    Version
     -------
    specification: Yohan Noël-huls (v.1 03/03/2018)
    """
    
    del elements[name]
    
    return(elements)
    
def collect(elements): 
    """Increment the element's content if it's an excavator and it is locked on an asteroid
    Parameter
    ---------
    elements: database of all the elements on the board (dict)
   
     Raise
     --------
     ValueError: elements must existed
     
     Version
     -------
     specification: Simon Rollus (v.1 03/03/2018)
    """
    
def drop_ore(player, element, current_money):
    """Drop the ore into the portal
    Parameter
    ---------
    player: the player who receives the ores (int)
    element: the excavator which contains the ores(dict)
    current_money: list of two elements containing the current money of both players (list)
    Raise
    --------
    ValueError: player must 0 or 1
    ValueError: database must exist
     
    Version
    -------
    specification: Yohan Noël-huls (v.1 03/03/2016)
    """
    current_money[player] += element['content']
    element['content'] = 0

def is_hit(hit,database):
    """Browse the database and return the elements which has been hit

    Parameters
    ----------
    hit: coordinates of the hit (dict)
    database: list of all the elements on the board (list)

    Return
    ------
    stricken: list of the elements which have been hit (list)
    
    Raise
     --------
     ValueError: hit must existed
     ValueError: database must existed
          
     Version
     -------
     specification: Yohan Noël-huls (v.1 03/03/201)
    """

def get_element_by_type (ship_type, database):
  """Return element(dic) by his type

     Parameters
     ----------
     ship_type : the type of the ship (str)
     database: database with all elements presented

     Raise
     --------
     ValueError: type must existed
     ValueError: data must existed
     
     Version
     -------
     specification: Yohan Noël-huls (v.1 03/03/2018)
     """


    
###------------------------------------------------------------------------------------------------------------
Schéma du bled
--------------

def file_to_data_base(file_name)
def ships_caracteristics_fonction()
def set_up_money()
def board_display(file_database,elements)
def AI_decision_making():
"""Order of the player"""
    def order_parser(order_0,order_1)
        def is_legal_move(order)
            -def ship_shifting(x,y,element)
            -def release_or_lock_order()
                 def drop_ore(player, element)      
            -def buy_order(ship_to_buy)
            -def attack_order(x_attack, y_attack, targeted_cases)
             def damage_applier(targeted_cases, database)
                 def is_hit(hit,database)
                 def element_destroy(element)
def collect(elements)
def board_display(file_database,elements)###





 

    
