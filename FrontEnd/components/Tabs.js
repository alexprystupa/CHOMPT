import React from 'react'
import {View, Text, StyleSheet, Image} from 'react-native'
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs'

import HomeScreen from '../screens/profileScreen'
import QuizScreen from '../screens/mapScreen'
import SocialScreen from '../screens/socialScreen'

const Tab = createBottomTabNavigator();

const Tabs = () => {
    return (
        <Tab.Navigator
            screenOptions = {{
                tabBarShowLabel: false,
                tabBarStyle: {
                    position: 'absolute',
                    bottom: 0,
                    left: 0,
                    right: 0,
                    elevation: 0,
                    backgroundColor: '#ffffff',
                    borderRadius: 0,
                    height: 90,
                }
            }}
        >
            <Tab.Screen name = "Profile" component = { HomeScreen } options = {{
                tabBarIcon: ({focused}) => (
                    <Image 
                        source = {require('../assets/icons/home.png')}
                        resizeMode = 'contain'
                        style = {{
                            width: 60,
                            height: 60,
                            tintColor: focused ? '#e32f45': '#748c94'
                        }}
                    />
                ),
            }}/>
            <Tab.Screen name = "Map Quiz Section" component = { QuizScreen } options = {{
                tabBarIcon: ({focused}) => (
                    <Image 
                        source = {require('../assets/icons/bread.png')}
                        resizeMode = 'contain'
                        style = {{
                            width: 60,
                            height: 60,
                            tintColor: focused ? '#e32f45': '#748c94'
                        }}
                    />
                ),
            }}/>
            <Tab.Screen name = "Social" component = { SocialScreen } options = {{
                tabBarIcon: ({focused}) => (
                    <Image 
                        source = {require('../assets/icons/hotdog.png')}
                        resizeMode = 'contain'
                        style = {{
                            width: 60,
                            height: 60,
                            tintColor: focused ? '#e32f45': '#748c94'
                        }}
                    />
                ),
            }}/>
        </Tab.Navigator>
    );
}

export default Tabs;