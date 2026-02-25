import { AppBar, Toolbar, Typography, makeStyles } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
    root: {
        background: "#802c6e",
        zIndex: 1,
        position: "fixed",
        height: "60px",
    },
    title: {
        width: "100%",
        fontWeight: "bold",
        display: "flex",
        alignItems: "center",
        [theme.breakpoints.down("xs")]: {
            justifyContent: "center",
        },
    },
}));

const Header = () => {
    const classes = useStyles();
    return (
        <>
            <AppBar className={classes.root}>
                <Toolbar className={classes.toolbar}>
                    <Typography className={classes.title} variant="h6">
                        Listado de Tareas
                    </Typography>
                </Toolbar>
            </AppBar>
        </>
    );
};

export default Header;
