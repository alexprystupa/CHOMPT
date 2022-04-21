import React from 'react'
import {View, Text, StyleSheet} from 'react-native'

const Footer = () => {
    return (
        <View style = {styles.footer}>
          <Text style = {styles.text}> LOGIN </Text>
        </View>
    );
};

const styles = StyleSheet.create({
    footer: {
        height: 60,
        padding: 15,
        backgroundColor: 'darkslateblue',
        bottom: -260
    },
    text: {
        color: '#fff',
        fontSize: 23,
        textAlign: 'center',
    },
});

export default Footer;