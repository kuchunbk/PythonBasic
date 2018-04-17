def Print_color(color_list_1,color_list_2):
    return(color_list_1.difference(color_list_2)) 


if __name__ == "__main__":
    color_list_1 = set(["White", "Black", "Red"]) 
    color_list_2 = set(["Red", "Green"])
    print(Print_color(color_list_1,color_list_2))