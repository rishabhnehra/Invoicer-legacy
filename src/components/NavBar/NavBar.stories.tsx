import {Story, Meta} from '@storybook/react/types-6-0';

import { NavBar as NavBarComponent, NavBarProps } from './NavBar';

export default {
    title: 'Components/Navigation Bar',
    component: NavBarComponent
} as Meta;

const Template: Story<NavBarProps> = (args) => <NavBarComponent {...args} />

export const NavigationBar = Template.bind({});
NavigationBar.args = {
    title: 'My Dashboard',
    isLoggedIn: true
}