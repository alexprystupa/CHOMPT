import React from 'react'
import { View, StyleSheet, TouchableOpacity, Button, Pressable, Text } from 'react-native';

const LoginButton = ({ onPress }) => {
    return(
        <Pressable
            title = "Login Button"
            color = "red"
            onPress = { onPress }
        />
    );
};

export default LoginButton;
