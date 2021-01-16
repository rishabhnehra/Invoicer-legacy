import {Story, Meta} from '@storybook/react/types-6-0';

import { Login as LoginComponent } from '../index';

export default {
    title: 'Components/Credentials Auth',
    component: LoginComponent
} as Meta;

const Template: Story = (args) => <LoginComponent {...args} />

export const Login = Template.bind({});
