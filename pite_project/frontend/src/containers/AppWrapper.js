import React from "react";

import Box from '@mui/material/Box';

const AppWrapper = ({ children }) => {
        return (
            <Box display="flex" flexDirection="column" minHeight="100vh" maxWidth="100vw" margin="0 auto">
                {children}
                <footer>Created by <a href="mailto:aleksandrar@student.agh.edu.pl">Aleksandra Rojek</a> & <a href="mailto:hrycalik@student.agh.edu.pl">Krzysztof Hrycalik</a></footer>
            </Box>
        );
};

export default AppWrapper;