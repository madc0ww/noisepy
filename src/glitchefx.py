#     ____ _     ___ _____ ____ _   _      _      ____    _____     _  _
#    / ___| |   |_ _|_   _/ ___| | | |    / \    |  _ \  |_   _|  _| || |
#   | |  _| |    | |  | || |   | |_| |   / _ \   | |_) |   | |   |_  ..  _|
#   | |_| | |___ | |  | || |___|  _  |  / ___ \  |  _ <    | |   |_      _|
#    \____|_____|___| |_| \____|_| |_| /_/   \_\ |_| \_\   |_|     |_||_|
#
# by
#      ___          ___         _____         ___          ___          ___
#     /__/\        /  /\       /  /::\       /  /\        /  /\        /__/\
#    |  |::\      /  /::\     /  /:/\:\     /  /:/       /  /::\      _\_ \:\
#    |  |:|:\    /  /:/\:\   /  /:/  \:\   /  /:/       /  /:/\:\    /__/\ \:\
#  __|__|:|\:\  /  /:/~/::\ /__/:/ \__\:| /  /:/  ___  /  /:/  \:\  _\_ \:\ \:\
# /__/::::| \:\/__/:/ /:/\:\\  \:\ /  /://__/:/  /  /\/__/:/ \__\:\/__/\ \:\ \:\
# \  \:\~~\__\/\  \:\/:/__\/ \  \:\  /:/ \  \:\ /  /:/\  \:\ /  /:/\  \:\ \:\/:/
#  \  \:\       \  \::/       \  \:\/:/   \  \:\  /:/  \  \:\  /:/  \  \:\ \::/
#   \  \:\       \  \:\        \  \::/     \  \:\/:/    \  \:\/:/    \  \:\/:/
#    \  \:\       \  \:\        \__\/       \  \::/      \  \::/      \  \::/
#     \__\/        \__\/                     \__\/        \__\/        \__\/
#
#  noisepy.py -- This belongs to noisepy
#
#  noisepy is a python module which implements methods for creating glitch art
#  pictures and movies
#
#  Copyright (C) 2017 madc0w - adriano mourao <madc0w@protonmail.ch>
#
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 3, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#  or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
#  for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import imageio

"""
colorChannel dic constant:
Color dictionary for translating RGB to
the numpy array position
"""
colorChannel = {'r' : 0, 'g' : 1, 'b' : 2}
"""
maxColorValue int constant
The maximum color value which each pixel can assume.
"""
maxColorValue = 255

def amplify(gain, channels, signal):
    # Copy input signal
    out = signal
    # Just a simple amp of each plane
    for ch in channels:
        out[:,:,colorChannel[ch]] = gain*signal[:,:,colorChannel[ch]]
    return out

def invert(channels, signal):
    out = maxColorValue - signal
    return out
