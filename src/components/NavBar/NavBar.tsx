import './NavBar.scss';

export type NavBarProps = {
    title: string,
    isLoggedIn: boolean
}

export const NavBar: React.FC<NavBarProps> = ({title, isLoggedIn}) => <div className="NavBar">
    <div className="container">
        <div className="left-side">
            <h3>{title}</h3>
        </div>
        {isLoggedIn && <div className="right-side">
            <a>My Account</a>
            <a>Logout</a>
        </div>}
    </div>
</div>