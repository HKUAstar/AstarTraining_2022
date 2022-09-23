PI = 3.1415926

# This function calculate the volumn of a cylinder
def volume_of_cylinder(radius, height):
    # calculate the area of bottom first
    bottom_area = PI * radius**2

    # multiply the bottom area and height to get the volume
    volume = bottom_area * height
    return volume


if __name__ == "__main__":
    ########## version 0 ##########

    v = 5*3.14 * 2**2 + 5*3.14*6**2 + 5 * 3.14 * 10**2
    print(v)

    h = 5
    r1, r2, r3 = 2, 6, 10
    pi = 3.14
    v1 = pi * r1**2 * h
    v2 = pi * r2**2 * h
    v3 = pi * r3**2 * h
    v = v1 + v2 + v3
    print(v)

    ###############################



    ########## version 1 ##########

    # we calculate the volume of each cylinder 
    volume_1 = volume_of_cylinder(2, 5) # r = 2, h = 5
    volume_2 = volume_of_cylinder(6, 5) # r = 6, h = 5
    volume_3 = volume_of_cylinder(10, 5) # r = 10, h = 5

    # sum up these three volumes
    total_volume = volume_1 + volume_2 + volume_3

    # output total_volume in 0.0001 precision
    print("total_volumn: %.4f", % (total_volume))

    ################################


    ########## version 2 ##########

    # init total_volume
    total_volume = 0

    # calculate each volume one by one and add it to total_volume
    for i in range(3):
        radius = 2 + 4 * i 
        height = 5
        total_volume += volume_of_cylinder(radius, height)

    # output total_volume in 0.0001 precision
    print("total_volumn: %.4f", % (total_volume))
    
    ################################
