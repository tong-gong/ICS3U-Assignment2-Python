#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a program to calculate the surface area of a cylinder.

import math


def main():
    # This is the function to calculate the surface area of the cylinder.

    # Input
    radius = int(input("Enter the radius of the cylinder (cm)"))
    height = int(input("Enter the height of the cylinder (cm)"))

    # Process
    surface_area = (math.pi * 2 * (radius ** 2) + 2 *
                    math.pi * height * radius)

    # Output
    print("")
    print("The surface area of the cylinder is {}cm".format(surface_area))


if __name__ == "__main__":
    main()
